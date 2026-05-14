import procesos
from datos import biblioteca, generos

def agregar_elemento():
    print("Agregar elemento")
    
    try:
        titulo = input("Ingrese el título del juego: ")
        genero = input("Ingrese el género del juego: ")
        año = int(input("Ingrese el año del juego: "))
        puntaje = float(input("Ingrese el puntaje del juego: "))
        
        procesos.procesar_agregar_elemento(titulo, genero, año, puntaje)
    except ValueError as error1:
        print("Error: Por favor, ingrese valores válidos para el año y el puntaje.")
        print(f"Detalles del error: {error1}")
    except Exception as error2:
        print(f"Error: {error2}")
    except puntaje < 0 or puntaje > 10:
        print("Error: El puntaje debe estar entre 0 y 10.")
    except not titulo or not genero:
        print("Error: El título y el género no pueden estar vacíos.")

def listar_todos_los_elementos():
    biblioteca_ordenada= sorted(biblioteca, key=lambda x : x["Puntaje"], reverse=True)
    
    for elemento in biblioteca_ordenada:
        print(f"[{elemento['id']:<2}] | Título: {elemento['Titulo']:<20} | Género: {elemento['Genero']:<20} | Año: {elemento['Año']:<5} | Puntuación: {elemento['Puntaje']}" )
        print("="*100)
        
def buscarPorTitulo():
    print("Buscar por título")

def filtrarPorGenero():
    print("Filtrar por género")

def filtrarPorAño():
    print("Filtrar por año")

def mostrarRecomendacionAleatoria():
    print("Mostrar recomendación aleatoria")

def eliminarElemento():
    print("Eliminar elemento")