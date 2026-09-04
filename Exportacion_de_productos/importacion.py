import json

def cargar_datos(ruta_archivo):
    """Lee el archivo JSON."""
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

def aplanar_productos(productos_crudos):
    """Convierte listas anidadas de productos en una sola lista plana."""
    productos_planos = []
    for item in productos_crudos:
        if isinstance(item, list):
            productos_planos.extend(item)
        else:
            productos_planos.append(item)
    return productos_planos
