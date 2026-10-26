def total_time_to_minutes(entrance_time, exit_time):
    """"
    Convierte el tiempo de entrada y salida en minutos totales.
    """
    entrance_hours, entrance_minutes = map(int, entrance_time.split(':'))
    exit_hours, exit_minutes = map(int, exit_time.split(':'))
    total_minutes = (exit_hours - entrance_hours) * 60 + (exit_minutes - entrance_minutes)
    return total_minutes


def calculate_parking_fee(total_minutes, vehicle_type, fees_to_charge):
    if total_minutes <= 0:
        return 0
    
    if total_minutes > 120:
        price_per_hour = fees_to_charge[vehicle_type]["precio_hora_adicional"]
        return price_per_hour + calculate_parking_fee(total_minutes - 60, vehicle_type, fees_to_charge)
    else:
        price_per_block = fees_to_charge[vehicle_type]["precio_bloque_30min"]
        return price_per_block + calculate_parking_fee(total_minutes - 30, vehicle_type, fees_to_charge)


def calculate_total_fee(total_minutes, days, vehicle_type, wash_service, fees_to_charge):
    match days:
        case 0:
            if wash_service:
                total_minutes -= 120
                base_fee = calculate_parking_fee(total_minutes, vehicle_type, fees_to_charge)
                return min(base_fee, fees_to_charge[vehicle_type]["tope_dia"]) + fees_to_charge[vehicle_type]["precio_lavado"]
                
            base_fee = calculate_parking_fee(total_minutes, vehicle_type, fees_to_charge)
            return min(base_fee, fees_to_charge[vehicle_type]["tope_dia"])
        case _:
            if wash_service:
                return fees_to_charge[vehicle_type]["precio_lavado"] + (days * fees_to_charge[vehicle_type]["tope_dia"])
            else:
                return days * fees_to_charge[vehicle_type]["tope_dia"]

 