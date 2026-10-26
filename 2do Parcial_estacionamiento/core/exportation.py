import os
import csv

EXPORTS_MAIN_FOLDER="exports/"
TICKETS_EXPORTATION_FOLDER_NAME= "Tickets"
MOVEMENTS_EXPORTATION_FOLDER_NAME= "Movimientos Procesados"
MANUAL_LIQUIDATION_FILE_NAME = "liquidacion-manual.csv"
ID_PREFIX = "OPM"


def find_path_folder(folder_name_to_find):
    core_directory = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(core_directory)
    folder_path = os.path.join(project_root, EXPORTS_MAIN_FOLDER+folder_name_to_find)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def create_id_movement():
    csv_folder_path = find_path_folder(MOVEMENTS_EXPORTATION_FOLDER_NAME)
    csv_file_path = os.path.join(csv_folder_path, MANUAL_LIQUIDATION_FILE_NAME)

    last_id_number = 0
    if os.path.isfile(csv_file_path) and os.path.getsize(csv_file_path) > 0:
        with open(csv_file_path, "r", newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
            if rows:
                last_id = rows[-1]["id"]
                last_id_number = int(last_id.replace(ID_PREFIX, ""))

    new_id_number = last_id_number + 1
    return f"{ID_PREFIX}{str(new_id_number).zfill(4)}"

## TICKETS ##

def create_ticket(
    checkout_list,
    base_parking_price,
    wash_service_cost,
    parking_with_wash_bonus,
    iva_included
    ):
    from datetime import datetime
    
    ticket_folder_path= find_path_folder(TICKETS_EXPORTATION_FOLDER_NAME)
    ticket_index=checkout_list.get("id").replace("OPM", "")
    ticket_name=f"TKT-{ticket_index}.txt".replace("OPM", "")
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
        file.write(f"Operación: {checkout_list["id"]}\n")
        file.write("\t"*9 + f"N° T. {ticket_index}\n")
        file.write(f"Fecha: {date.day:<2}/{date.month:<2}/{date.year:<20}Hora: {date.hour:<2}:{date.minute:<2}:{date.second:<2}\n")
        file.write(f"Patente: {checkout_list["patente"]:<7}\n")
        file.write(f"Vehiculo: {checkout_list["tipo_vehiculo"]:<10}\n")
        file.write(f"\n")
        if checkout_list["dias"] == 0:
            file.write(f"Horario: {checkout_list["hora_entrada"]:<5} - {checkout_list["hora_salida"]:<5}\n")
            file.write("\t"*10 + f"${base_parking_price:<5}\n")
        else:
            file.write(f"Dias estacionados: {checkout_list["dias"]:<2}\n")
            file.write("\t"*10 + f"${base_parking_price:<5}\n")
        
        if checkout_list["solicito_lavado"]:
            file.write("Servicio de lavado: Solicitado\n")
            file.write("\t"*10 + f"${wash_service_cost:<5}\n")
            if checkout_list["dias"]== 0:
                file.write("Bonificación de lavado primeras 2 horas\n")
                file.write("\t"*9 + f"   -${parking_with_wash_bonus:<5}\n")
        else: 
            file.write("Servicio de lavado: No solicitado\n")
        
        file.write(f"Subtotal:"+"\t"*8 + f"${checkout_list["total_cobrado"]}\n")
        file.write("-"*58)
        file.write("\nREGIMEN DE TRANSPARENCIA FISCAL AL CONSUMIDOR (Ley 27.743)\n")
        file.write(f"IVA contenido: ${iva_included}\n")
        file.write("LOS IMPUESTOS INFORMADOS SON LOS QUE \nCORRESPONDEN A NIVEL NACIONAL\n")
        file.write("-"*58)



## MOVIMIENTOS PROCESADOS ##

def create_csv(dictionary_list, file_name,csv_mode):
    if not dictionary_list: return
    csv_folder_path=find_path_folder(MOVEMENTS_EXPORTATION_FOLDER_NAME)
    csv_exported_file= os.path.join(csv_folder_path, file_name)

    columns=dictionary_list[0].keys()
    file_exists = os.path.isfile(csv_exported_file)
    needs_header = (csv_mode == "w") or (not file_exists) or (file_exists and os.path.getsize(csv_exported_file) == 0)
    
    with open(csv_exported_file, csv_mode, newline="", encoding="utf-8") as file:
        file_writer=csv.DictWriter(file, fieldnames=columns)
        if needs_header:
            file_writer.writeheader()
        file_writer.writerows(dictionary_list)
    
    