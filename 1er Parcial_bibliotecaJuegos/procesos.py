import funcionesMenu
from datos import biblioteca, generos

def procesar_ordenar_por_puntaje(biblioteca_a_ordenar):
    return sorted(biblioteca_a_ordenar, key=lambda x : x["Puntaje"], reverse=True)


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


def procesar_encontrar_elementos(titulo_buscado):
    titulo_buscado_minuscula = titulo_buscado.lower()
    
    titulos_encontrados = [e for e in biblioteca if titulo_buscado_minuscula in e["Titulo"].lower()]
    
    if titulos_encontrados:
        return titulos_encontrados[:]
    else:
        return None