import time
import os
import sys

import funcionesMenu
from datos import biblioteca, generos

""""
NO VA CON LA CONSIGNA PERO LO DEJO POR SI QUIERO AGREGARLO DESPUES
    
* Agregar el nuevo género a la lista de géneros disponibles si no existe.  
def agregar_genero(genero_a_agregar_en_lista):
    generos.append(genero_a_agregar_en_lista)
    print(f"Nuevo género '{genero_a_agregar_en_lista}' agregado a la lista de géneros disponibles.")
    # RECORDAR DESCOMENTAR LA FUNCIÓN EN procesar_agregar_elemento Y CAMBIAR generos A LISTA SI SE USA LA FUNCIÓN.
"""
def mensaje_volviendo_al_menu():
    print("\nVolviendo al menú principal...")
    time.sleep(2.5)

def limpiar_pantalla():
    #Windows
    if os.name == 'nt': 
        os.system('cls')
    #Linux / macOS
    else: 
        os.system('clear')


def getch():
    """Lee una sola tecla del teclado sin esperar a que se presione Enter."""
    # Windows
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8', errors='ignore')
    
    # Linux / macOS
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def mover_cursor(linea, columna):
    """Mueve el cursor a la posición especificada en la terminal.
    Args:
        linea (int): El número de línea a la que se desea mover el cursor.
        columna (int): El número de columna a la que se desea mover el cursor.
    """
    sys.stdout.write(f"\033[{linea};{columna}H")
    sys.stdout.flush()


def procesar_ordenar_por_puntaje(biblioteca_a_ordenar):
    return sorted(biblioteca_a_ordenar, key=lambda x : x["Puntaje"], reverse=True)


def procesar_agregar_elemento(titulo_a_agregar, genero_a_agregar, año_a_agregar, puntaje_a_agregar):
    longitud_original = len(biblioteca)
    
    try:
        nuevo_elemento = {
            "id" : len(biblioteca) + 1,
            "Titulo" : titulo_a_agregar,
            "Genero" : genero_a_agregar,
            "Año" : año_a_agregar,
            "Puntaje" : puntaje_a_agregar
            }
        biblioteca.append(nuevo_elemento)
        
        
        """
        if genero_a_agregar not in generos:
            agregar_genero(genero_a_agregar)
        """
        return len(biblioteca) > longitud_original
    except Exception as error:
        print(f"Error al agregar el elemento. \n{error}")
        return False


def validar_generos_ingresados(genero_ingresado):
    """Valida géneros ingresados por el usuario.
    Args:
        genero_ingresado (str): Cadena con géneros separados por comas.

    Returns:
        tuple: (genero_normalizado, generos_invalidos)
            genero_normalizado (str|None): Géneros válidos formateados.
            generos_invalidos (list): Géneros no reconocidos.
    """
    generos_disponibles = {g.lower(): g for g in generos} # convierte la lista de generos a minusculas
    generos_ingresados = [g.strip() for g in str(genero_ingresado).split(",") if g.strip()] # separa los generos ingresados por comas, elimina espacios y términos nulos.

    if not generos_ingresados:
        return None, []

    generos_invalidos = [g for g in generos_ingresados if g.lower() not in generos_disponibles]
    if generos_invalidos:
        return None, generos_invalidos

    genero_normalizado = ", ".join(generos_disponibles[g.lower()] for g in generos_ingresados) # Convierte los géneros ingresados a su formato original (con mayúscula inicial y espacios)
    return genero_normalizado, []


def procesar_encontrar_elementos(clave_a_buscar, valor_buscado):
    """Función para encontrar elementos en la biblioteca según una clave y un valor específico. La búsqueda es insensible a mayúsculas y minúsculas.
    Args:
        clave_a_buscar (str): La clave por la cual se desea buscar (por ejemplo, "Titulo", "Genero", etc.).
        valor_buscado (str): El valor que se desea encontrar en la clave especificada.
    Returns:
        list: Una lista de elementos que coinciden con el valor buscado. Si no se encuentra ningún elemento, devuelve None.
    """
    valor_buscado = str(valor_buscado).lower() # Convertir el valor buscado a string en minúsculas
    
    try:
        elementos_encontrados = [e for e in biblioteca if valor_buscado in str(e[clave_a_buscar]).lower()] # Convierte la clave a buscar a string para evitar errores si se ingresa un número
    except KeyError as error1:
        print(f"Error: La clave '{clave_a_buscar}' no existe en los elementos de la biblioteca. \nError: {error1}")
        return None
    except Exception as error2:
        print(f"Error al buscar elementos. \n{error2}")
        return None
    
    
    if elementos_encontrados:
        return elementos_encontrados
    else:
        return None
    
def mostrar_lista(valores_a_mostrar):
    try:
        print("="*100)
        for elemento in valores_a_mostrar:
            print(f"[{elemento['id']:<2}] | Título: {elemento['Titulo']:<20} | Género: {elemento['Genero']:<20} | Año: {elemento['Año']:<5} | Puntuación: {elemento['Puntaje']}" )
            print("="*100)
    except Exception as error:
        print(f"Error al mostrar la lista. \n{error}")
        
def mostrar_recomendacuion_aleatoria():
    import random
    if biblioteca:
        recomendacion = random.choice(biblioteca)
        mostrar_lista([recomendacion]) # Mostrar la recomendación como una lista de un solo elemento
    else:
        print("ERROR: La biblioteca está vacía. No se pueden mostrar recomendaciones.")
        
        
def procesar_eliminar_elemento(id_a_eliminar):
    """Función para eliminar un elemento de la biblioteca según su ID.
    Args:
        id_a_eliminar (int): El ID del elemento a eliminar.
    Returns:
        bool: True si se eliminó un elemento, False si no se encontró el ID.
    """
    try:
        longitud_original = len(biblioteca)
        biblioteca[:] = [e for e in biblioteca if e["id"] != id_a_eliminar] # Actualiza el contenido de la lista compartida
        return len(biblioteca) < longitud_original
    except Exception as error:
        print(f"Error al eliminar el elemento. \n{error}")
        return False