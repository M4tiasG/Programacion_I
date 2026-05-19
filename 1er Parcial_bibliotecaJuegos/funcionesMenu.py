from procesos import *
from datos import biblioteca, generos


def agregar_elemento():
    # Imprime el menú completo para más comodidad del usuario.
    limpiar_pantalla()
    print("="*37)
    print("AGREGAR ELEMENTO A LA BIBLIOTECA")
    print("="*37)
    print("Ingrese el título del juego: ")
    print("Ingrese los géneros del juego (separados por comas): ")
    print("Ingrese el año del juego: ")
    print("Ingrese el puntaje del juego: \n")
    print("Géneros disponibles: " + ", ".join(generos)) # join para mostrar los strings sin forma de lista/tupla.

    try:
        # Mover el cursor a las posiciones para ingresar los datos, ingresarlos, validarlos, repetir.
        mover_cursor(4, 30) 
        titulo = input().strip()
        assert titulo != "", "El título no puede estar vacío."
        
        mover_cursor(5, 54)
        genero = input().strip()
        assert genero != "", "El género no puede estar vacío."
        

        # Validar géneros ingresados por el usuario.
        genero, generos_invalidos = validar_generos_ingresados(genero)
        if genero is None:
            limpiar_pantalla()
            if generos_invalidos:
                print(f"Error: El/Los género(s) '{', '.join(generos_invalidos)}' no se encuentra(n) en la lista de géneros disponibles.")
            else:
                print("Error: Debe ingresar al menos un género válido.")
            mensaje_volviendo_al_menu()
            return

        mover_cursor(6, 27)
        año = int(input())
        assert año != None, "El año no puede estar vacío."
        assert año > 0, "El año debe ser un número positivo."
        assert año <= 2026, "No se pueden agregar juegos de años futuros."
        
        
        mover_cursor(7, 31)
        puntaje = float(input())
        assert puntaje > 0 and puntaje <= 10, "El puntaje debe ser un número entre 0 y 10."
        assert puntaje != None, "El puntaje no puede estar vacío."
        assert isinstance(puntaje, float), "El puntaje debe ser un número."


        if procesar_agregar_elemento(titulo, genero, año, puntaje):
            limpiar_pantalla()
            print("Elemento agregado correctamente.")
            mensaje_volviendo_al_menu()
        else:
            limpiar_pantalla()
            print("Hubo un error y no se pudo agregar el elemento a la biblioteca.")
            mensaje_volviendo_al_menu()
    except ValueError:
        limpiar_pantalla()
        print("Error: Se ingresaron valores no válidos.")
        mensaje_volviendo_al_menu()
    except AssertionError as error:
        limpiar_pantalla()
        print(f"Error: {error}")
        mensaje_volviendo_al_menu()

def listar_todos_los_elementos():
    biblioteca_ordenada= procesar_ordenar_por_puntaje(biblioteca)
    print("="*37)
    print("LISTA DE VIDEOJUEGOS EN LA BIBLIOTECA")
    print("="*37)
    mostrar_lista(biblioteca_ordenada)
    print("\nPresione Cualquier tecla para volver al menú principal.")
    getch()

def buscarPorTitulo():
    try:
        titulo_buscado = input("Ingrese el título del juego a buscar: ").strip()
        
        if not titulo_buscado:
            print("Error: El título no puede estar vacío.")
            mensaje_volviendo_al_menu()
            return

        valores_encontrados = procesar_encontrar_elementos("Titulo", titulo_buscado) #Encontrar elementos
        valores_encontrados = procesar_ordenar_por_puntaje(valores_encontrados) # Ordenar por puntaje
        
        if valores_encontrados != None:
            mostrar_lista(valores_encontrados)
        else:
            print("ERROR: No se encontró ningún videojuego con el título ingresado.")
            mensaje_volviendo_al_menu()
            return
    except ValueError as error:
        print(f"ERROR: Ingrese un valor correcto.\nError: {error}")
        mensaje_volviendo_al_menu()


def filtrarPorGenero():
    print("Géneros disponibles: " + ", ".join(generos)) # join para mostrar los strings sin forma de tupla
    
    genero_buscado = input("Ingrese los géneros a buscar (separados por comas): ").strip()
    if not genero_buscado:
        print("Error: El género no puede estar vacío.")
        mensaje_volviendo_al_menu()
        return
    
    valores_encontrados = procesar_encontrar_elementos("Genero", genero_buscado) #Encontrar elementos
    
    if valores_encontrados != None:
        mostrar_lista(valores_encontrados)
    else:
        print("ERROR: No se encontró ningún videojuego con el Género ingresado.")
        mensaje_volviendo_al_menu()


def filtrarPorAño():
    try:
        anio_buscado = int(input("Ingrese el año del juego a buscar: "))
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico para el año.")
        return

    if not anio_buscado:
        print("Error: El año no puede estar vacío.")
        mensaje_volviendo_al_menu()
        return

    valores_encontrados = procesar_encontrar_elementos("Año", anio_buscado) #Encontrar elementos

    if valores_encontrados != None:
        mostrar_lista(valores_encontrados)
    else:
        print("ERROR: No se encontró ningún videojuego con el año ingresado.")
        mensaje_volviendo_al_menu()

def mostrar_recomendacion_aleatoria():
    print("="*37)
    print("MOSTRAR RECOMENDACIÓN ALEATORIA")
    print("="*37)
    mostrar_recomendacuion_aleatoria()

def eliminar_elemento():
    print("="*37)
    print("ELIMINAR ELEMENTO")
    print("="*37)
    try:
        id_a_eliminar = int(input("Ingrese el ID del juego a eliminar: "))
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico para el ID.")
        return
    if not id_a_eliminar:
        print("Error: El ID no puede estar vacío.")
        return
    
    # Confirmación antes de eliminar
    print("="*37)
    print("ADVERTENCIA")
    print("="*37)
    print("Está seguro que desea eliminar el elemento con ID " + str(id_a_eliminar) + "?\n Esta acción no se puede deshacer. (s/n)")
    confirmacion = input().strip().lower()
    if confirmacion != "s":
        print("Eliminación cancelada. Volviendo al menú principal.")
        time.sleep(2.5)
        return

    # Proceso de eliminación
    if procesar_eliminar_elemento(id_a_eliminar):
        print(f"Elemento con ID {id_a_eliminar} eliminado correctamente. Volviendo al menú principal.")
        time.sleep(2.5)
    else:
        print(f"No se encontró ningún elemento con ID {id_a_eliminar}.")