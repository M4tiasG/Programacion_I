print("\nINGRESAR UN CARACER PARA SALIR DEL PROGRAMA.\n")
while True:
    try:
        x=int(input("Ingrese un número: "))
    except ValueError:
        print("Saliendo del programa...\n")  
        break
    
    if x%2 == 0:
        print("El numero ingresado es par.\n")
    else:
        print("El numero ingresado es impar.\n")