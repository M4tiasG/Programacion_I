from validations import *
from importation import extract_fees_prices

import customtkinter as ctk   

def process_fee():
    try:
        plate_raw= plate_entry_text_box.get()
        vehicle_type_raw= vehicle_type_option_menu.get()
        days_raw= days_entry_text_box.get()
        wash_service_raw= bool(wash_service_checkbox.get())
        
        clean_plate= validate_vehicle_plate(plate_raw)
        assert clean_plate , "Patente con formato incorrecto"
        clean_vehicle_type= validate_vehicle_type(vehicle_type_raw)
        assert clean_vehicle_type, "Vehiculo incorrecto"
        clean_days= int(days_raw)
        total_time=0
        
        if clean_days == 0:
            clean_entrance_time= entrance_time_text_box.get()
            clean_exit_time= exit_time_text_box.get()
            assert validate_time_format(clean_entrance_time), "Horario de entrada incorrecto"
            assert validate_time_format(clean_exit_time), "Horario de entrada incorrecto"
            total_time= total_time_to_minutes(clean_entrance_time, clean_exit_time)
            assert total_time > 0, "Horario inconsistente"
    
        fees_prices= extract_fees_prices()
        total_fee=calculate_total_fee(total_time, clean_days, clean_vehicle_type, wash_service_raw, fees_prices)
        
        print("Patente: ", clean_plate)
        print("Tipo V: ", clean_vehicle_type)
        print("Dias: ", clean_days)
        print("solicito lavado: ", wash_service_raw)
        if clean_days == 0:
            print("hora entrada: ", clean_entrance_time)
            print("hora salida: ", clean_exit_time)
            print("total minutos: ", total_time)
        print("precio final: ", total_fee)
    except AssertionError as error:
        print(f"ERROR: {error}")
        return
    except ValueError as error:
        print(f"ERROR: {error}")
        return

window=ctk.CTk()
window.title("Sistema AutoPark")
window.geometry("400x550") # ancho x alto

window_title_label=ctk.CTkLabel(window, text= "Cobro en ventanilla", font=("Arial", 20, "bold"))
window_title_label.pack(pady=20)

plate_subtitle_label=ctk.CTkLabel(window, text= "Patente", font=("Arial", 12))

plate_entry_text_box=ctk.CTkEntry(
    window,
    placeholder_text="AAA000...",
    font=("Arial", 16),
    width=200
    )
plate_subtitle_label.pack(pady=1)
plate_entry_text_box.pack(pady=5)

vehicle_type_subtitle_label=ctk.CTkLabel(window, text= "Tipo de Vehículo", font=("Arial", 12))

vehicle_type_option_menu=ctk.CTkOptionMenu(
    window,
    values= ["Seleccione un vehiculo..."] + list(ALLOWED_VEHICLES)
    )
vehicle_type_subtitle_label.pack(pady=1)
vehicle_type_option_menu.pack(pady=5)

days_subtitle_label=ctk.CTkLabel(window, text= "Dias pasados", font=("Arial", 12))
days_entry_text_box=ctk.CTkEntry(
    window,
    placeholder_text="0",
    font=("Arial", 16),
    width=200
    )
days_subtitle_label.pack(pady=1)
days_entry_text_box.pack(pady=5)

entrance_time_subtitle_label=ctk.CTkLabel(window, text= "Hora de entrada", font=("Arial", 12))
entrance_time_text_box=ctk.CTkEntry(
    window,
    placeholder_text="HH:MM",
    font=("Arial", 16),
    width=200
    )
entrance_time_subtitle_label.pack(pady=1)
entrance_time_text_box.pack(pady=5)

exit_time_subtitle_label=ctk.CTkLabel(window, text= "Hora de salida", font=("Arial", 12))
exit_time_text_box=ctk.CTkEntry(
    window,
    placeholder_text="HH:MM",
    font=("Arial", 16),
    width=200
    )
exit_time_subtitle_label.pack(pady=1)
exit_time_text_box.pack(pady=5)

wash_service_checkbox=ctk.CTkCheckBox(window, text= "¿Solicitó servicio de lavado?")
wash_service_checkbox.pack(pady=15)


btn_finish = ctk.CTkButton(window,
    text="Liquidar", 
    font=("Arial", 12, "bold"), 
    height=40,
    command=process_fee)
btn_finish.pack(pady=10)

window.mainloop()