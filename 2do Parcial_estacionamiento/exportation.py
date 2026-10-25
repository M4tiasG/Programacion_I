import os
import csv

TICKETS_EXPORTATION_FOLDER_NAME= "Tickets"
MOVEMENTS_EXPORTATION_FOLDER_NAME= "Movimientos Procesados"


def find_path_folder(folder_name_to_find):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path= os.path.join(current_directory, folder_name_to_find)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

## TICKETS ##
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
    ticket_folder_path= find_path_folder(TICKETS_EXPORTATION_FOLDER_NAME)
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


## HISTORY MOVEMENTS ##

def create_csv(dictionary_list, file_name):
    if not dictionary_list: return
    csv_folder_path=find_path_folder(MOVEMENTS_EXPORTATION_FOLDER_NAME)
    csv_exported_file= os.path.join(csv_folder_path, file_name)

    columns=dictionary_list[0].keys()
    with open(csv_exported_file, "w", newline="", encoding="utf-8") as file:
        file_writer=csv.DictWriter(file, fieldnames=columns)
        file_writer.writeheader()
        file_writer.writerows(dictionary_list)
    
    