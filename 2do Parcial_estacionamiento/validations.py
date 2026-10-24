from calculations import *
import re

ALLOWED_VEHICLES=("auto", "moto", "camioneta")
PLATES_PATTERNS = {
        "argentina": r'^[A-Z]{3}\d{3}$',
        "mercosur": r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    }

def validate_vehicle_plate(plate):
    clean_plate = plate.replace(" ", "").upper()
    for pattern in PLATES_PATTERNS.values():
        if re.match(pattern, clean_plate):
            return clean_plate

def validate_vehicle_type(vehicle_type):
    clean_vehicle_type = vehicle_type.replace(" ", "").lower()
    if clean_vehicle_type in ALLOWED_VEHICLES:
        return clean_vehicle_type

def validate_time_format(time_str):
    if re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', time_str):
        return time_str

""""
def validate_movements(flatten_parking_history_movements, flatten_fees_prices):
    valid_parking_movements=[]
    invalid_valid_parking_movements=[]
    try:
        for movement in flatten_parking_history_movements:
            id_raw=movement.get("id")
            plate_raw=movement.get("patente")
            vehicle_type_raw= movement.get("tipo_vehiculo")
            entrance_time_raw=movement.get("entrada")
            exit_time_raw=movement.get("salida")
            wash_service_raw=movement.get("solicito_lavado")
            
            if not validate_vehicle_plate(plate_raw):
                movement["motivo_rechazo"]= "Patente invalida"
                invalid_valid_parking_movements.append(movement)
                continue
            if not validate_vehicle_type(vehicle_type_raw):
                movement["motivo_rechazo"]= "Tipo de vehiculo invalido"
                invalid_valid_parking_movements.append(movement)
                continue
            if not validate_time_format(entrance_time_raw):
                movement["motivo_rechazo"]= "Hora de entrada invalida"
                invalid_valid_parking_movements.append(movement)
                continue
            if not validate_time_format(exit_time_raw):
                movement["motivo_rechazo"]= "Hora de salida invalida"
                invalid_valid_parking_movements.append(movement)
                continue
            
    except AssertionError as error:
"""