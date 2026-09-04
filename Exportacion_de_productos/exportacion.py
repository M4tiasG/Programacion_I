import csv
import os

def configurar_exportacion():
    """Solicita al usuario los parámetros para exportar los CSV."""
    # Separador
    separador = ','
    while True:
        op = input("Elige el separador (1 para coma ',', 2 para punto y coma ';'): ")
        if op == '1': break
        if op == '2': 
            separador = ';'
            break
        print("Opción no válida.")

    # Ordenamiento
    mapa_orden = {'1': 'nombre', '2': 'precio', '3': 'stock'}
    campo_orden = 'nombre'
    while True:
        op = input("Elige por qué campo ordenar (1: Nombre, 2: Precio, 3: Stock): ")
        if op in mapa_orden:
            campo_orden = mapa_orden[op]
            break
        print("Opción no válida.")

    # Dirección
    reverso = False
    while True:
        op = input("Elige la dirección (1: Ascendente, 2: Descendente): ")
        if op == '1': break
        if op == '2':
            reverso = True
            break
        print("Opción no válida.")
    return separador, campo_orden, reverso

def generar_archivos_csv(directorio_programa, productos_validos, separador, campo_orden, reverso):
    """Agrupa los productos por usuario y genera los archivos CSV."""
    
    carpeta_salida = os.path.join(directorio_programa, "salida_csv")
    
    # Crea la carpeta si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    
    productos_por_usuario = {}
    for p in productos_validos:
        id_user = p['id_usuario']
        if id_user not in productos_por_usuario:
            productos_por_usuario[id_user] = []
        productos_por_usuario[id_user].append(p)

    columnas_csv = ['id', 'nombre', 'categoria', 'precio', 'stock']

    for id_user, lista_productos in productos_por_usuario.items():
        lista_productos.sort(key=lambda x: x[campo_orden], reverse=reverso)
        nombre_archivo = f"productos_{id_user}.csv"
        
        # define la ruta para exportarse dento de una subcarpeta.
        ruta_archivo = os.path.join(carpeta_salida, nombre_archivo)
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.DictWriter(archivo_csv, fieldnames=columnas_csv, delimiter=separador)
            escritor.writeheader()
            for prod in lista_productos:
                # Filtrar solo las claves que van en el CSV
                fila = {col: prod[col] for col in columnas_csv}
                escritor.writerow(fila)
        
        print(f"Archivo exportado: salida_csv/{nombre_archivo} ({len(lista_productos)} productos)")