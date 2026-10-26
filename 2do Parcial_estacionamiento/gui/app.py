import customtkinter as ctk

window = None
frame_main_menu = None
frame_checkout = None

# -- variables de COBRO EN VENTANILLA --
days_subtitle_label= None
entrance_time_subtitle_label= None
exit_time_subtitle_label= None

plate_entry_text_box = None
vehicle_type_option_menu = None
multi_day_checkbox = None
days_entry_text_box = None
entrance_time_text_box = None
exit_time_text_box = None
wash_service_checkbox = None

def create_window():
    global window, frame_main_menu, frame_checkout
    window = ctk.CTk()
    window.title("Sistema AutoPark")
    window.geometry("400x600")
    frame_main_menu = ctk.CTkFrame(window)
    frame_checkout = ctk.CTkFrame(window)