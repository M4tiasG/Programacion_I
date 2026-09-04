import os
from validaciones import *
from importacion import *
from exportacion import *

def main():
    # Setea directorio actual y busca .json
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(directorio_actual, "productos.json")
    
    if not os.path.exists(ruta_json):
        print(f"Error: No se encontró el archivo en la ruta:\n{ruta_json}")
        return
    # Importar
    datos = cargar_datos(ruta_json)
    usuarios = datos.get("usuarios", [])
    productos_crudos = datos.get("productos", [])
    usuarios_validos = {u['id_usuario'] for u in usuarios}
    
    # Validar
    productos_planos = aplanar_productos(productos_crudos)
    productos_validos, productos_rechazados = normalizar_y_validar(productos_planos, usuarios_validos)

    # Imprimir rechazados
    print("\n--- REPORTE DE PRODUCTOS RECHAZADOS ---")
    if not productos_rechazados:
        print("Todos los productos fueron validados con éxito.")
    for rechazado in productos_rechazados:
        print(f"❌ {rechazado['producto']} -> Motivo(s): {rechazado['motivos']}")
    print("-" * 39 + "\n")

    if not productos_validos:
        print("No hay productos válidos para exportar. Finalizando programa.")
        return

    # Exportar resultados validos
    separador, campo, reverso = configurar_exportacion()
    print("\n--- GENERANDO ARCHIVOS ---")
    generar_archivos_csv(directorio_actual, productos_validos, separador, campo, reverso)

if __name__ == "__main__":
    main()