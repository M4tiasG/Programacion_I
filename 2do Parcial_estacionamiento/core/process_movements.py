from core.validations import *
from core.calculations import *
from core.importation import *
from core.exportation import create_csv

# ver forma de instalar customtkinter y CTkMessagebox al iniciar el programa

def process_history_movements():
    
    fees_prices= extract_fees_prices()
    
    parking_history_json_path=find_path(PARKING_HISTORY_JSON)
    parking_history_structure=import_json_configuration(parking_history_json_path)
    parking_history_movements=parking_history_structure.get("movimientos", [])
    flatten_parking_history_movements=flatten_json_dictionary(parking_history_movements)
    
    valid_parking_movements=[]
    invalid_parking_movements=[]
    
    for movement in flatten_parking_history_movements:
        id_raw=movement.get("id")
        plate_raw=movement.get("patente")
        vehicle_type_raw= movement.get("tipo_vehiculo")
        entrance_time_raw=movement.get("entrada")
        exit_time_raw=movement.get("salida")
        wash_service_raw=movement.get("solicito_lavado")

        clean_plate= validate_vehicle_plate(plate_raw)
        if not clean_plate:
            movement["motivo_rechazo"]= "Patente invalida"
            invalid_parking_movements.append(movement)
            continue
        
        clean_vehicle_type= validate_vehicle_type(vehicle_type_raw)
        if not clean_vehicle_type:
            movement["motivo_rechazo"]= f"Tipo de vehiculo invalido"
            invalid_parking_movements.append(movement)
            continue
        if not validate_time_format(entrance_time_raw):
            movement["motivo_rechazo"]= "Hora de entrada invalida"
            invalid_parking_movements.append(movement)
            continue
        if not validate_time_format(exit_time_raw):
            movement["motivo_rechazo"]= "Hora de salida invalida"
            invalid_parking_movements.append(movement)
            continue
    
        total_time=total_time_to_minutes(entrance_time_raw, exit_time_raw)
        if total_time < 0:
            movement["motivo_rechazo"]= "Hora inconsistente"
            invalid_parking_movements.append(movement)
            continue
        
        total_fee=calculate_total_fee(total_time, 0, clean_vehicle_type, wash_service_raw, fees_prices)
        movement["total_cobrado"]= total_fee
        
        movement["patente"]=clean_plate
        movement["tipo_vehiculo"]=clean_vehicle_type
        valid_parking_movements.append(movement)
        
    create_csv(valid_parking_movements, "liquidacion.csv")
    create_csv(invalid_parking_movements, "rechazados.csv")
    return True
