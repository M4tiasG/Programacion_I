from funcionesMenu import *

def main():
    while True:
        print("\n\nBiblioteca de videojuegos")
        print("1. Agregar elemento")
        print("2. Listar todos los elementos")
        print("3. Buscar por título")
        print("4. Filtrar por género")
        print("5. Filtrar por año")
        print("6. Mostrar recomendación aleatoria")
        print("7. Eliminar elemento")
        print("8. Salir")
        
        try:
            opcion = int(input("Ingrese una opción: "))
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
                    mostrarRecomendacionAleatoria()
                case 7:
                    eliminarElemento()
                case 8:
                    break
                case _:
                    print("Opción inválida.")
        except ValueError as error:
            print(f"ERROR: Ingrese un valor correcto. \n{error}")

if __name__=="__main__":
    main()