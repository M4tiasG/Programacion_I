import customtkinter as ctk
import gui.app as app
from gui.controllers import *
from core.validations import ALLOWED_VEHICLES

def build_plate_section():
    plate_subtitle_label=ctk.CTkLabel(app.frame_checkout, text= "Patente", font=("Arial", 12))
    app.plate_entry_text_box=ctk.CTkEntry(
        app.frame_checkout,
        placeholder_text="AAA000...",
        font=("Arial", 16),
        width=200
        )
    plate_subtitle_label.pack(pady=1)
    app.plate_entry_text_box.pack(pady=5)


def build_vehicle_type_section():
    vehicle_type_subtitle_label=ctk.CTkLabel(app.frame_checkout, text= "Tipo de Vehículo", font=("Arial", 12))
    app.vehicle_type_option_menu=ctk.CTkOptionMenu(
        app.frame_checkout,
        values= ["Seleccione un vehiculo..."] + list(ALLOWED_VEHICLES)
        )
    vehicle_type_subtitle_label.pack(pady=1)
    app.vehicle_type_option_menu.pack(pady=5)


def build_multi_day_checkbox_section():
    app.multi_day_var = ctk.IntVar(value=0)
    app.multi_day_checkbox = ctk.CTkCheckBox(
        app.frame_checkout,
        text="Estadía de varios días",
        variable=app.multi_day_var,
        command=toggle_multi_day_mode
    )
    app.multi_day_checkbox.pack(pady=5)

def buil_days_section():
    app.days_subtitle_label=ctk.CTkLabel(app.frame_checkout, text= "Dias pasados", font=("Arial", 12))
    app.days_entry_text_box=ctk.CTkEntry(
            app.frame_checkout,
            placeholder_text="0...",
            font=("Arial", 16),
            width=200,
            state="disabled"
        )


def buil_entrance_hour_section():
    app.entrance_time_subtitle_label=ctk.CTkLabel(app.frame_checkout, text= "Hora de entrada", font=("Arial", 12))
    app.entrance_time_text_box=ctk.CTkEntry(
        app.frame_checkout,
        placeholder_text="HH:MM...",
        font=("Arial", 16),
        width=200
        )
    app.entrance_time_subtitle_label.pack(pady=1)
    app.entrance_time_text_box.pack(pady=5)
    
    
def buil_exit_hour_section():
    app.exit_time_subtitle_label=ctk.CTkLabel(app.frame_checkout, text= "Hora de salida", font=("Arial", 12))
    app.exit_time_text_box=ctk.CTkEntry(
        app.frame_checkout,
        placeholder_text="HH:MM...",
        font=("Arial", 16),
        width=200
        )
    app.exit_time_subtitle_label.pack(pady=1)
    app.exit_time_text_box.pack(pady=5)


def build_wash_service_section():
    app.wash_service_checkbox=ctk.CTkCheckBox(app.frame_checkout, text= "¿Solicitó servicio de lavado?")
    app.wash_service_checkbox.pack(pady=15)


def build_views():
    # --- MENÚ PRINCIPAL ---
    main_menu_title_label = ctk.CTkLabel(app.frame_main_menu, text="Sistema AutoPark", font=("Arial", 24, "bold"))
    main_menu_title_label.pack(pady=40)

    btn_checkout= ctk.CTkButton(
        app.frame_main_menu,
        text="Cobro en Ventanilla", 
        command=show_checkout_window)
    btn_checkout.pack(pady=10)

    btn_process_movements=ctk.CTkButton(
        app.frame_main_menu,
        text="Procesar lote de movimientos", 
        command=action_btn_process_movements)
    btn_process_movements.pack(pady=10)

    btn_cerrar = ctk.CTkButton(
        app.frame_main_menu, 
        text="Cerrar",
        fg_color="#E7180B",
        hover_color="#9F0712",
        command= close_program)
    btn_cerrar.pack(pady=10)


    # --- COBRO EN VENTANILLA ---
    window_title_label=ctk.CTkLabel(
        app.frame_checkout, text= "Cobro en ventanilla", font=("Arial", 20, "bold"))
    window_title_label.pack(pady=20)

    # BOTON VOLVER
    btn_back_main_menu=ctk.CTkButton(
        app.frame_checkout, 
        text="< Volver al Menú", 
        command=show_main_menu_window)
    btn_back_main_menu.pack(pady=10)
    # PATENTE
    build_plate_section()
    # VEHICULO
    build_vehicle_type_section()
    # DIAS
    build_multi_day_checkbox_section()
    buil_days_section()
    # TIEMPO ENTRADA
    buil_entrance_hour_section()
    # TIEMPO SALIDA
    buil_exit_hour_section()
    # SERVICIO DE LAVADO
    build_wash_service_section()
    # BOTON LIQUIDAR
    btn_finish = ctk.CTkButton(app.frame_checkout,
        text="Liquidar", 
        font=("Arial", 12, "bold"), 
        height=40,
        command=process_chekout)
    btn_finish.pack(pady=10)
    
    app.frame_main_menu.pack(fill="both", expand=True)