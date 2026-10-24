from validations import *
from calculations import *
from importation import *

FEES_CONFIGURATION_JSON= "tarifas.json"
PARKING_HISTORY_JSON="movimientos.json"

if __name__ == "__main__":
    
    fees_configuration_json_path=find_path(FEES_CONFIGURATION_JSON)
    parking_history_json_path=find_path(PARKING_HISTORY_JSON)
    
    fee_structure=import_json_configuration(fees_configuration_json_path)
    parking_history_structure=import_json_configuration(parking_history_json_path)
    
    parking_history_movements=parking_history_structure.get("movimientos", [])
    fees_prices=fee_structure.get("tarifas", {})
    
    flatten_parking_history_movements=flatten_json_dictionary(parking_history_movements)
    flatten_fees_prices=flatten_json_dictionary(fees_prices)
    
    valid_parking_movements=[]
    invalid_valid_parking_movements=[]
    for movement in flatten_parking_history_movements:
        id_raw=movement.get("id")
        plate_raw=movement.get("patente")
        vehicle_type_raw= movement.get("tipo_vehiculo")
        entrance_time_raw=movement.get("entrada")
        exit_time_raw=movement.get("salida")
        wash_service_raw=movement.get("solicito_lavado")

        cleand_plate= validate_vehicle_plate(plate_raw)
        if not cleand_plate:
            movement["motivo_rechazo"]= "Patente invalida"
            invalid_valid_parking_movements.append(movement)
            continue
        
        clean_vehicle_type= validate_vehicle_type(vehicle_type_raw)
        if not clean_vehicle_type:
            movement["motivo_rechazo"]= f"Tipo de vehiculo invalido"
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
    
        total_time=total_time_to_minutes(entrance_time_raw, exit_time_raw)
        if total_time < 0:
            movement["motivo_rechazo"]= "Hora inconsistente"
            invalid_valid_parking_movements.append(movement)
            continue
        
        total_fee=calculate_total_fee(total_time, 0, clean_vehicle_type, wash_service_raw, fees_prices)
        movement["total_cobrado"]= total_fee
        valid_parking_movements.append(movement)

    print("validos: ", len(valid_parking_movements))
    print("invalidos: ", len(invalid_valid_parking_movements))
    print("id y motivo de los invalidos: ")
    for invalid in invalid_valid_parking_movements:
        print(f"id: {invalid.get('id')}, motivo: {invalid.get('motivo_rechazo')}")
