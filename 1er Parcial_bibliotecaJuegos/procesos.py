import funcionesMenu
from datos import biblioteca, generos

def procesar_agregar_elemento(titulo, genero, año, puntaje):
    try:
        nuevo_elemento = {
            "id" : len(biblioteca) + 1,
            "Titulo" : titulo,
            "Genero" : genero,
            "Año" : año,
            "Puntaje" : puntaje
            }
        biblioteca.append(nuevo_elemento)
    except Exception as error:
        print(f"Error al agregar el elemento: {error}")