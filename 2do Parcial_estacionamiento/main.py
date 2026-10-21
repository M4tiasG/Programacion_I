from validations import *
from calculations import *

if __name__ == "__main__":
    """"
    plate = input("Ingrese la patente del vehiculo: ")
    validated_plate = validate_vehicle_plate(plate)
    if validated_plate:
        print(f"Patente validada: {validated_plate}")
    else:
        print("Patente invalida.")
    """
    print(validate_time_format("23:00"))  # Ejemplo de uso
    print(total_time_to_minutes("10:30", "12:15"))  # Ejemplo de uso