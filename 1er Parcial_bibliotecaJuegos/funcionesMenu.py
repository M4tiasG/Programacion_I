from procesos import *
from datos import *


def agregar_elemento():
    print("="*37)
    print(f"{NEGRITA}AGREGAR ELEMENTO A LA BIBLIOTECA{RESET}")
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
                print(f"{ROJO}{NEGRITA}Error:{RESET} El/Los género(s) {ROJO}{NEGRITA}'{', '.join(generos_invalidos)}'{RESET} no se encuentra(n) en la lista de géneros disponibles.")
            else:
                print(f"{ROJO}{NEGRITA}Error:{RESET} Debe ingresar al menos un género válido.")
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
            print(f"{VERDE}Elemento agregado correctamente.{RESET}")
            mensaje_volviendo_al_menu()
        else:
            limpiar_pantalla()
            print("Hubo un error y no se pudo agregar el elemento a la biblioteca.")
            mensaje_volviendo_al_menu()
    except ValueError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} Se ingresaron valores no válidos. {error}")
        mensaje_volviendo_al_menu()
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return

def listar_todos_los_elementos():
    try:
        assert len(biblioteca) > 0, "La biblioteca está vacía."
        
        biblioteca_ordenada= procesar_ordenar_por_puntaje(biblioteca)
        print("="*37)
        print(f"{NEGRITA}LISTA DE VIDEOJUEGOS EN LA BIBLIOTECA{RESET}")
        print("="*37)
        mostrar_lista(biblioteca_ordenada)
        print("\nPresione Cualquier tecla para volver al menú principal.")
        getch()
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return


def buscarPorTitulo():
    print("="*37)
    print(f"{NEGRITA}BUSCAR POR TITULO{RESET}")
    print("="*37)
    print("--Nota: el titulo puede estar parcialmente completo--")
    print("Ingrese el título del juego a buscar: ", end="")
    try:
        titulo_buscado = input().strip()
        assert titulo_buscado != "", "El título no puede estar vacío."

        valores_encontrados = procesar_encontrar_elementos("Titulo", titulo_buscado) #Encontrar elementos
        
        
        if valores_encontrados is not None:
            valores_encontrados = procesar_ordenar_por_puntaje(valores_encontrados) # Ordenar por puntaje
            
            limpiar_pantalla()
            print(f"== {NEGRITA}VIDEOJUEGOS COINCIDENTES CON '{titulo_buscado}'{RESET} ==")
            mostrar_lista(valores_encontrados)
            print("\nPresione Cualquier tecla para volver al menú principal.")
            getch()
        else:
            limpiar_pantalla()
            print("No se encontró ningún videojuego con el título ingresado.")
            mensaje_volviendo_al_menu()
            return
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return


def filtrarPorGenero():
    print("="*37)
    print(f"{NEGRITA}FILTRAR POR GENERO{RESET}")
    print("="*37)
    print("Géneros disponibles: " + ", ".join(generos)) # join para mostrar los strings sin forma de tupla
    print("Ingrese el género a buscar: ", end="")
    
    try:
        genero_buscado = input().strip()
        assert genero_buscado != "", "El género no puede estar vacío."
        
        valores_encontrados = procesar_encontrar_elementos("Genero", genero_buscado) #Encontrar elementos
        
        if valores_encontrados is not None:
            valores_encontrados = procesar_ordenar_por_puntaje(valores_encontrados)
            limpiar_pantalla()
            print(f"=={NEGRITA} VIDEOJUEGOS COINCIDENTES CON EL GENERO '{genero_buscado}'{RESET} ==")
            mostrar_lista(valores_encontrados)
            print("\nPresione Cualquier tecla para volver al menú principal.")
            getch()
        else:
            print(f"No se encontró ningún videojuego con el género '{genero_buscado}'.")
            mensaje_volviendo_al_menu()
            return
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return


def filtrarPorAño():
    print("="*37)
    print(f"{NEGRITA}FILTRAR POR AÑO{RESET}")
    print("="*37)
    print("Ingrese el año del juego año a buscar: ", end="")
    try:
        anio_buscado = int(input())
        assert anio_buscado != None, "El año no puede estar vacío."
        assert isinstance(anio_buscado, int), "El año debe ser un número entero."
        assert anio_buscado > 0, "El año debe ser un número positivo."
        
        valores_encontrados = procesar_encontrar_elementos("Año", anio_buscado) #Encontrar elementos

        if valores_encontrados is not None:
            valores_encontrados = procesar_ordenar_por_puntaje(valores_encontrados)
            limpiar_pantalla()
            print(f"== {NEGRITA}VIDEOJUEGOS DEL AÑO {anio_buscado}{RESET} ==")
            mostrar_lista(valores_encontrados)
            print("\nPresione Cualquier tecla para volver al menú principal.")
            getch()
        else:
            limpiar_pantalla()
            print(f"No se encontró ningún videojuego del año {anio_buscado}.")
            mensaje_volviendo_al_menu()
    except ValueError as error:
        print(f"Error: Por favor, ingrese un valor numérico para el año. {error}")
        mensaje_volviendo_al_menu()
        return
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return
    

def mostrar_recomendacion_aleatoria():
    print("="*37)
    print(f"{NEGRITA}RECOMENDACION ALEATORIA{RESET}")
    print("="*37)
    mostrar_recomendacuion_aleatoria()
    print("\nPresione Cualquier tecla para volver al menú principal.")
    getch()

def eliminar_elemento():
    print("="*37)
    print(f"{NEGRITA}ELIMINAR ELEMENTO{RESET}")
    print("="*37)
    try:
        id_a_eliminar = int(input("Ingrese el ID del juego a eliminar: "))
        assert id_a_eliminar != None, "El ID no puede estar vacío."
        assert isinstance(id_a_eliminar, int), "El ID debe ser un número entero."
        assert id_a_eliminar > 0, "El ID debe ser un número positivo."
        
        
        
    except ValueError as error:
        limpiar_pantalla()
        print(f"Error: Por favor, ingrese un valor numérico para el ID. {error}")
        mensaje_volviendo_al_menu()
        return
    except AssertionError as error:
        limpiar_pantalla()
        print(f"{ROJO}{NEGRITA}Error:{RESET} {error}")
        mensaje_volviendo_al_menu()
        return
    
    # Confirmación antes de eliminar
    limpiar_pantalla()
    print("="*37)
    print(f"{NEGRITA}{AMARILLO}ADVERTENCIA{RESET}")
    print("="*37)
    print("Está seguro que desea eliminar el elemento con ID " + str(id_a_eliminar) + f"?\n{ROJO}{NEGRITA}Esta acción no se puede deshacer.{RESET} \n(s/n) >> ", end="")
    
    confirmacion = input().strip().lower()
    if confirmacion != "s":
        limpiar_pantalla()
        print("Eliminación cancelada por el usuario.")
        mensaje_volviendo_al_menu()
        return

    # Proceso de eliminación
    if procesar_eliminar_elemento(id_a_eliminar):
        limpiar_pantalla()
        print(f"{VERDE}Elemento con ID {id_a_eliminar} eliminado correctamente.{RESET}")
        mensaje_volviendo_al_menu()
        return
    else:
        limpiar_pantalla()
        print(f"No se encontró ningún elemento con ID {id_a_eliminar}.")
        mensaje_volviendo_al_menu()
        return