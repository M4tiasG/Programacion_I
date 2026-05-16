from procesos import *
from datos import biblioteca, generos

def agregar_elemento():
    print("Agregar elemento")
    
    try:
        titulo = input("Ingrese el título del juego: ").strip()
        genero = input("Ingrese el género del juego: ").strip()
        
        if not titulo or not genero:
            print("Error: El título y el género no pueden estar vacíos.")
            return

        año = int(input("Ingrese el año del juego: "))
        puntaje = float(input("Ingrese el puntaje del juego: "))
        
        if puntaje < 0 or puntaje > 10:
            print("Error: El puntaje debe estar entre 0 y 10.")
            return

        procesar_agregar_elemento(titulo, genero, año, puntaje)
    except ValueError:
        print("Error: Por favor, ingrese valores válidos para el año y el puntaje.")

def listar_todos_los_elementos():
    biblioteca_ordenada= procesar_ordenar_por_puntaje(biblioteca)
    
    for elemento in biblioteca_ordenada:
        print(f"[{elemento['id']:<2}] | Título: {elemento['Titulo']:<20} | Género: {elemento['Genero']:<20} | Año: {elemento['Año']:<5} | Puntuación: {elemento['Puntaje']}" )
        print("="*100)
        
def buscarPorTitulo():
    try:
        titulo_buscado = input("Ingrese el título del juego a buscar: ").strip()
        
        if not titulo_buscado:
            print("Error: El título no puede estar vacío.")
            return

        valores_encontrados = procesar_encontrar_elementos(titulo_buscado) #Encontrar elementos
        valores_encontrados = procesar_ordenar_por_puntaje(valores_encontrados) # Ordenar por puntaje
        
        if valores_encontrados != None:
            print("="*100)
            for elemento in valores_encontrados:
                print(f"[{elemento['id']:<2}] | Título: {elemento['Titulo']:<20} | Género: {elemento['Genero']:<20} | Año: {elemento['Año']:<5} | Puntuación: {elemento['Puntaje']}" )
                print("="*100)
        else:
            print("ERROR: No se encontró el elemento.")
    except ValueError as error:
        print(f"ERROR: Ingrese un valor correcto.\nError: {error}")


def filtrarPorGenero():
    print("Filtrar por género")

def filtrarPorAño():
    print("Filtrar por año")

def mostrarRecomendacionAleatoria():
    print("Mostrar recomendación aleatoria")

def eliminarElemento():
    print("Eliminar elemento")