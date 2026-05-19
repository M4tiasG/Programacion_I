from funcionesMenu import *
from procesos import *
from datos import *


def main():
    while True:
        limpiar_pantalla()
        print("="*37)
        print(f"{NEGRITA}BIBLIOTECA DE VIDEOJUEGOS{RESET}")
        print("="*37)
        print("1. Agregar elemento")
        print("2. Listar todos los elementos")
        print("3. Buscar por título")
        print("4. Filtrar por género")
        print("5. Filtrar por año")
        print("6. Mostrar recomendación aleatoria")
        print("7. Eliminar elemento")
        print("="*37)
        print("8. Salir")
        
        try:
            opcion = int(getch())
            limpiar_pantalla()
            match opcion:
                case 1:
                    agregar_elemento()
                case 2:
                    listar_todos_los_elementos()
                case 3:
                    buscarPorTitulo()
                case 4:
                    filtrarPorGenero()
                case 5:
                    filtrarPorAño()
                case 6:
                    mostrar_recomendacion_aleatoria()
                case 7:
                    eliminar_elemento()
                case 8:
                    break
                case _:
                    print("\nOpción inválida.")
                    time.sleep(0.8)
        except ValueError as error:
            print(f"ERROR: Ingrese un valor numérico. \n{error}")
            time.sleep(2.5)

if __name__=="__main__":
    main()