import os

def find_path_ticket_folder():
    folder_name="Tickets"
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path= os.path.join(current_directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def create_ticket_index(ticket_folder_path):
    tickets_folder=os.listdir(ticket_folder_path)
    current_indexes=0
    for file in tickets_folder:
        if file.startswith("TKT-") and file.endswith(".txt"):
            current_indexes+=1
    new_index=current_indexes+1
    new_index=str(new_index).zfill(4)
    return new_index


def create_ticket(plate, vehicle_type, days, entrance_time, exit_time, wash_service, subtotal):
    ticket_folder_path= find_path_ticket_folder()
    ticket_index=create_ticket_index(ticket_folder_path)
    ticket_name=f"TKT-{ticket_index}.txt"
    
    ticket_exported_file = os.path.join(ticket_folder_path, ticket_name)
    with open(ticket_exported_file, "w", encoding="utf-8") as file:
        file.write("==============================\n")
        file.write("       AUTOPARK TICKET        \n")
        file.write("==============================\n")
        file.write(f"Patente: {plate}\n")
        file.write(f"Vehiculo: {vehicle_type}\n")
        if days == 0:
            file.write(f"Horario: {entrance_time} - {exit_time}\n")
        else:
            file.write(f"Dias estacionados: {days}\n")
        file.write(f"Servicio de lavado: {wash_service}\n")
        file.write(f"Subtotal: {subtotal}\n")