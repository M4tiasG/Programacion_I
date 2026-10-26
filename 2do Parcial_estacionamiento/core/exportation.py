import os
import csv

TICKETS_EXPORTATION_FOLDER_NAME= "exports/Tickets"
MOVEMENTS_EXPORTATION_FOLDER_NAME= "exports/Movimientos Procesados"


def find_path_folder(folder_name_to_find):
    core_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(core_directory)
    folder_path = os.path.join(project_root, folder_name_to_find)
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


def create_ticket(plate, 
    vehicle_type, 
    days, 
    entrance_time, 
    exit_time, 
    wash_service, 
    subtotal,
    base_parking_price,
    wash_service_cost,
    parking_with_wash_bonus,
    iva_included
    ):
    from datetime import datetime
    
    ticket_folder_path= find_path_folder(TICKETS_EXPORTATION_FOLDER_NAME)
    ticket_index=create_ticket_index(ticket_folder_path)
    ticket_name=f"TKT-{ticket_index}.txt"
    date=datetime.now()
    
    ticket_exported_file = os.path.join(ticket_folder_path, ticket_name)
    with open(ticket_exported_file, "w", encoding="utf-8") as file:
        file.write("="*46 + "\n")
        file.write("AUTOPARK S.A.S.\n")
        file.write("C.U.I.T. Nro: 30539523410\n")
        file.write("Ing. brutos: 30-20385849-0\n")
        file.write("Cordoba 2062 - 3300 - Posadas - Misiones\n")
        file.write("IVA Responable Inscripto\n")
        file.write("A CONSUMIDOR FINAL\n")
        file.write("="*46 + "\n")
        file.write("\t"*9 + f"N° T. {ticket_index}\n")
        file.write(f"Fecha: {date.day:<2}/{date.month:<2}/{date.year:<20}Hora: {date.hour:<2}:{date.minute:<2}:{date.second:<2}\n")
        file.write(f"Patente: {plate:<7}\n")
        file.write(f"Vehiculo: {vehicle_type:<10}\n")
        if days == 0:
            file.write(f"Horario: {entrance_time:<5} - {exit_time:<5}\n")
            file.write("\t"*10 + f"${base_parking_price:<5}\n")
        else:
            file.write(f"Dias estacionados: {days:<2}\n")
            file.write("\t"*10 + f"${base_parking_price:<5}\n")
        
        if wash_service:
            file.write("Servicio de lavado: Solicitado\n")
            file.write("\t"*10 + f"${wash_service_cost:<5}\n")
            if days== 0:
                file.write("Bonificación de lavado primeras 2 horas\n")
                file.write("\t"*9 + f"   -${parking_with_wash_bonus:<5}\n")
        else: 
            file.write("Servicio de lavado: No solicitado\n")
        
        file.write(f"Subtotal:"+"\t"*8 + f"${subtotal}\n")
        file.write("-"*58)
        file.write("\nREGIMEN DE TRANSPARENCIA FISCAL AL CONSUMIDOR (Ley 27.743)\n")
        file.write(f"IVA contenido: ${iva_included}\n")
        file.write("LOS IMPUESTOS INFORMADOS SON LOS QUE \nCORRESPONDEN A NIVEL NACIONAL\n")
        file.write("-"*58)



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
    
    