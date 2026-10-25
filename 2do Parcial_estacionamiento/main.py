from validations import *
from importation import extract_fees_prices
from exportation import create_ticket
from process_movements import process_history_movements

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox 

def show_checkout_window():
    frame_main_menu.pack_forget()
    frame_checkout.pack(fill="both", expand=True)
    
def show_main_menu_window():
    frame_checkout.pack_forget()
    frame_main_menu.pack(fill="both", expand=True)
    
def action_btn_process_movements():
    try:
        assert process_history_movements, "Ocurrió un error al exportar los movimientos"
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
    window.destroy()


def process_chekout():
    try:
        clean_plate= validate_vehicle_plate(plate_entry_text_box.get())
        assert clean_plate , "Patente con formato incorrecto"
        clean_vehicle_type= validate_vehicle_type(vehicle_type_option_menu.get())
        assert clean_vehicle_type, "Vehiculo incorrecto"
        clean_days= int(days_entry_text_box.get())
        clean_wash_service= bool(wash_service_checkbox.get())
        total_time=0
        clean_entrance_time= None
        clean_exit_time= None
        
        if clean_days == 0:
            clean_entrance_time= entrance_time_text_box.get()
            clean_exit_time= exit_time_text_box.get()
            assert validate_time_format(clean_entrance_time), "Horario de entrada incorrecto"
            assert validate_time_format(clean_exit_time), "Horario de entrada incorrecto"
            total_time= total_time_to_minutes(clean_entrance_time, clean_exit_time)
            assert total_time > 0, "Horario inconsistente"
            
        fees_prices= extract_fees_prices()
        total_fee=calculate_total_fee(total_time, clean_days, clean_vehicle_type, clean_wash_service, fees_prices)
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
        
        total_fee_message_box= CTkMessagebox(
            title="Información - Liquidar estacionamiento",
            message=f"Total a pagar: {total_fee}",
            icon= "check",
            option_1="Imprimir Comprobante",
        )
        option_selected=total_fee_message_box.get()
        if option_selected == "Imprimir Comprobante":
            create_ticket(
                clean_plate,
                clean_vehicle_type,
                clean_days,
                clean_entrance_time,
                clean_exit_time,
                clean_wash_service,
                total_fee
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


if __name__== "__main__":
    window=ctk.CTk()
    window.title("Sistema AutoPark")
    window.geometry("400x550") # ancho x alto

    message_box=ctk.CTk()
    message_box.geometry("200x300")

    frame_main_menu=ctk.CTkFrame(window)
    frame_checkout=ctk.CTkFrame(window)
    # frame_process_movements=ctk.CTkFrame(window)

    ### MENU PRINCIPAL ### 
    
    main_menu_title_label = ctk.CTkLabel(frame_main_menu, text="Sistema AutoPark", font=("Arial", 24, "bold"))
    main_menu_title_label.pack(pady=40)
    
    btn_checkout= ctk.CTkButton(frame_main_menu,
        text="Cobro en Ventanilla", 
        command=show_checkout_window)
    btn_checkout.pack(pady=10)
    
    btn_process_movements=ctk.CTkButton(frame_main_menu,
        text="Procesar lote de movimientos", 
        command=action_btn_process_movements)
    btn_process_movements.pack(pady=10)
    
    btn_cerrar = ctk.CTkButton(
        frame_main_menu, 
        text="Cerrar", 
        command= close_program)
    btn_cerrar.pack(pady=40)
    
    
    ### COBRO VENTANILLA ###
    window_title_label=ctk.CTkLabel(frame_checkout, text= "Cobro en ventanilla", font=("Arial", 20, "bold"))
    window_title_label.pack(pady=20)

    btn_back_main_menu=ctk.CTkButton(
        frame_checkout, 
        text="< Volver al Menú", 
        command=show_main_menu_window)
    btn_back_main_menu.pack(pady=10)

    plate_subtitle_label=ctk.CTkLabel(frame_checkout, text= "Patente", font=("Arial", 12))
    plate_entry_text_box=ctk.CTkEntry(
        frame_checkout,
        placeholder_text="AAA000...",
        font=("Arial", 16),
        width=200
        )
    plate_subtitle_label.pack(pady=1)
    plate_entry_text_box.pack(pady=5)

    vehicle_type_subtitle_label=ctk.CTkLabel(frame_checkout, text= "Tipo de Vehículo", font=("Arial", 12))

    vehicle_type_option_menu=ctk.CTkOptionMenu(
        frame_checkout,
        values= ["Seleccione un vehiculo..."] + list(ALLOWED_VEHICLES)
        )
    vehicle_type_subtitle_label.pack(pady=1)
    vehicle_type_option_menu.pack(pady=5)

    days_subtitle_label=ctk.CTkLabel(frame_checkout, text= "Dias pasados", font=("Arial", 12))
    days_entry_text_box=ctk.CTkEntry(
        frame_checkout,
        placeholder_text="0",
        font=("Arial", 16),
        width=200
        )
    days_subtitle_label.pack(pady=1)
    days_entry_text_box.pack(pady=5)

    entrance_time_subtitle_label=ctk.CTkLabel(frame_checkout, text= "Hora de entrada", font=("Arial", 12))
    entrance_time_text_box=ctk.CTkEntry(
        frame_checkout,
        placeholder_text="HH:MM",
        font=("Arial", 16),
        width=200
        )
    entrance_time_subtitle_label.pack(pady=1)
    entrance_time_text_box.pack(pady=5)

    exit_time_subtitle_label=ctk.CTkLabel(frame_checkout, text= "Hora de salida", font=("Arial", 12))
    exit_time_text_box=ctk.CTkEntry(
        frame_checkout,
        placeholder_text="HH:MM",
        font=("Arial", 16),
        width=200
        )
    exit_time_subtitle_label.pack(pady=1)
    exit_time_text_box.pack(pady=5)

    wash_service_checkbox=ctk.CTkCheckBox(frame_checkout, text= "¿Solicitó servicio de lavado?")
    wash_service_checkbox.pack(pady=15)


    btn_finish = ctk.CTkButton(frame_checkout,
        text="Liquidar", 
        font=("Arial", 12, "bold"), 
        height=40,
        command=process_chekout)
    btn_finish.pack(pady=10)

    frame_main_menu.pack(fill="both", expand=True)
    window.mainloop()