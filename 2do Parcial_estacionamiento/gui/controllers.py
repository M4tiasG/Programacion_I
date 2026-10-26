from core.validations import validate_vehicle_plate, validate_vehicle_type, validate_time_format
from core.calculations import total_time_to_minutes, calculate_total_fee, calculate_parking_fee
from core.importation import extract_fees_prices
from core.exportation import create_ticket, create_csv, create_id_movement
from core.process_movements import process_history_movements
import gui.app as app

from CTkMessagebox import CTkMessagebox

def resize_window_to_content():
    app.window.update_idletasks()   
    active_frame = app.frame_checkout if app.frame_checkout.winfo_ismapped() else app.frame_main_menu
    width = active_frame.winfo_reqwidth() + 150
    height = active_frame.winfo_reqheight() + 20
    app.window.geometry(f"{width}x{height}")


def show_checkout_window():
    app.frame_main_menu.pack_forget()
    app.frame_checkout.pack(fill="both", expand=True)
    resize_window_to_content()
    
def show_main_menu_window():
    app.frame_checkout.pack_forget()
    app.frame_main_menu.pack(fill="both", expand=True)
    resize_window_to_content()
    
    
def toggle_multi_day_mode():
    if app.multi_day_var.get() == 1:
        app.days_entry_text_box.configure(state="normal")
        
        app.entrance_time_text_box.configure(state="normal")
        app.entrance_time_text_box.delete(0, "end")
        app.entrance_time_text_box.configure(state="disabled")
        
        app.exit_time_text_box.configure(state="normal")
        app.exit_time_text_box.delete(0, "end")
        app.exit_time_text_box.configure(state="disabled")
        
        app.days_subtitle_label.pack(pady=1, before=app.wash_service_checkbox)
        app.days_entry_text_box.pack(pady=5, before=app.wash_service_checkbox)
        
        app.entrance_time_subtitle_label.pack_forget()
        app.exit_time_subtitle_label.pack_forget()
        app.entrance_time_text_box.pack_forget()
        app.exit_time_text_box.pack_forget()
    else:
        app.days_entry_text_box.configure(state="normal")
        app.days_entry_text_box.delete(0, "end")
        app.days_entry_text_box.configure(state="disabled")
        
        app.entrance_time_text_box.configure(state="normal")
        app.exit_time_text_box.configure(state="normal")
        
        app.entrance_time_subtitle_label.pack(pady=1, before=app.wash_service_checkbox)
        app.entrance_time_text_box.pack(pady=5, before=app.wash_service_checkbox)
        app.exit_time_subtitle_label.pack(pady=1, before=app.wash_service_checkbox)
        app.exit_time_text_box.pack(pady=5, before=app.wash_service_checkbox)
        
        app.days_subtitle_label.pack_forget()
        app.days_entry_text_box.pack_forget()
    resize_window_to_content()
    
    
def action_btn_process_movements():
    try:
        assert process_history_movements(), "Ocurrió un error al exportar los movimientos"
        correct_msg_box= CTkMessagebox(
                                title=f"Información - Procesar lote de movimientos",
                                message="Se procesaron los lotes de movimiento a CSV's",
                                icon= "check",
                            )
    except AssertionError as error:
            assertion_error_msg_box= CTkMessagebox(
                        title=f"Error en los datos",
                        message=f"ERROR: {error}. Verifique los datos y vuelva a intentarlo.",
                        icon= "cancel",
                    )
            # Console debug
            print(f"ERROR: {error}")
            return
        
        
def close_program():
    app.window.destroy()


def process_chekout():
    from datetime import datetime
    manual_checkout_record={
        "id": create_id_movement(), # En caso de error en algún Assert se borra ID.
    }
    
    try:
        fees_prices= extract_fees_prices()
        # VARIBALES PARA CALCULOS BASICOS DE TOTAL
        clean_plate= validate_vehicle_plate(app.plate_entry_text_box.get())
        assert clean_plate , "Patente con formato incorrecto"
        
        clean_vehicle_type= validate_vehicle_type(app.vehicle_type_option_menu.get())
        assert clean_vehicle_type, "Vehiculo incorrecto"
        
        days_raw=app.days_entry_text_box.get().strip()
        clean_days= int(days_raw) if days_raw else 0
        assert clean_days >= 0, "Los días no pueden ser negativos"
        
        clean_wash_service= bool(app.wash_service_checkbox.get())
        
        total_time=0
        clean_entrance_time= None
        clean_exit_time= None
        # VARIABLES PARA EL DESGLOSE EN TICKET
        wash_service_cost= 0
        base_parking_price=0
        parking_with_wash_bonus= 0
        iva_included=0
        
        if clean_days == 0:
            clean_entrance_time= app.entrance_time_text_box.get()
            clean_exit_time= app.exit_time_text_box.get()
            assert validate_time_format(clean_entrance_time), "Horario de entrada incorrecto"
            assert validate_time_format(clean_exit_time), "Horario de entrada incorrecto"
            
            total_time= total_time_to_minutes(clean_entrance_time, clean_exit_time)
            assert total_time > 0, "Horario inconsistente"
            
            base_parking_price=min(calculate_parking_fee(total_time, clean_vehicle_type, fees_prices),fees_prices[clean_vehicle_type]["tope_dia"])
        else:
            base_parking_price= clean_days*fees_prices[clean_vehicle_type]["tope_dia"]
        
        if clean_wash_service: wash_service_cost= fees_prices[clean_vehicle_type]["precio_lavado"]
        # Subtotal
        total_fee=calculate_total_fee(total_time, clean_days, clean_vehicle_type, clean_wash_service, fees_prices)
        
        parking_with_wash_bonus= base_parking_price + wash_service_cost - total_fee
        iva_included=total_fee*0.21
        
        manual_checkout_record.update({
            "fecha": datetime.now().strftime("%d/%m/%Y"),
            "hora": datetime.now().strftime("%H:%M:%S"),
            "patente": clean_plate,
            "tipo_vehiculo": clean_vehicle_type,
            "dias": clean_days,
            "hora_entrada": clean_entrance_time if clean_days == 0 else "",
            "hora_salida": clean_exit_time if clean_days == 0 else "",
            "solicito_lavado": clean_wash_service,
            "total_cobrado": total_fee,
        })
        """"
        # Console debug
        print("Patente: ", clean_plate)
        print("Tipo V: ", clean_vehicle_type)
        print("Dias: ", clean_days)
        print("solicito lavado: ", clean_wash_service)
        if clean_days == 0:
            print("hora entrada: ", clean_entrance_time)
            print("hora salida: ", clean_exit_time)
            print("total minutos: ", total_time)
            print("precio final: ", total_fee)
        """
        
        total_fee_message_box= CTkMessagebox(
            title="Información - Liquidar estacionamiento",
            message=f"Total a pagar: {total_fee}",
            icon= "check",
            option_1="Registrar e imprimir ticket",
            option_2="Cancelar"
        )
        option_selected=total_fee_message_box.get()
        if option_selected == "Registrar e imprimir ticket":
            create_csv([manual_checkout_record], "liquidacion-manual.csv", "a")
            create_ticket(
                manual_checkout_record,
                base_parking_price,
                wash_service_cost,
                parking_with_wash_bonus,
                iva_included
            )
    except AssertionError as error:
        assertion_error_msg_box= CTkMessagebox(
                    title=f"Error en los datos",
                    message=f"ERROR: {error}. Verifique los datos y vuelva a intentarlo.",
                    icon= "cancel",
                )
        # Console debug
        print(f"ERROR: {error}")
        return
    except ValueError as error:
        value_error_msg_box= CTkMessagebox(
                            title=f"Error en los datos",
                            message=f"ERROR: {error}. Verifique los datos y vuelva a intentarlo.",
                            icon= "cancel",
                        )
        print(f"ERROR: {error}")
        return