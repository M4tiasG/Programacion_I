import json
import os

def find_path(file_to_search):
    base_directory= os.path.dirname(os.path.abspath(__file__))
    json_path=os.path.join(base_directory, file_to_search)
    if not json_path:
        print(f"ERROR configurate_path: No se pudo encontrar el archivo {file_to_search}")
    return json_path

def import_json_configuration(json_config_path):
    """
    Loads and returns the JSON data from the specified configuration file.

    Parameters:
        json_config_path (str): Path to the JSON configuration file.

    Returns:
        dict: The parsed JSON data as a Python dictionary.
    """
    with open (json_config_path, "r", encoding="utf-8") as file:
        return json.load(file)

def flatten_json_dictionary(array_to_process):
    flatten_parking_history=[]
    for item in array_to_process:
        if isinstance(item, list):
            flatten_parking_history.extend(item)
        else:
            flatten_parking_history.append(item)
    return flatten_parking_history