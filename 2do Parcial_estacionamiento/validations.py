from configuration import ALLOWED_VEHICLES
import re

def validate_vehicle_plate(plate):
    clean_plate = plate.replace(" ", "").upper()
    # Ver si colocar estos patrones en un archivo de configuracion
    patterns = {
        "argentina": r'^[A-Z]{3}\d{3}$',
        "mercosur": r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    }
    for pattern in patterns.values():
        if re.match(pattern, clean_plate):
            return clean_plate

def validate_vehicle_type(vehicle_type):
    clean_vehicle_type = vehicle_type.replace(" ", "").lower()
    if clean_vehicle_type in ALLOWED_VEHICLES:
        return clean_vehicle_type

def validate_time_format(time_str):
    if re.match(r'^(?:[01]\d|2[0-3]):[0-5]\d$', time_str):
        return time_str