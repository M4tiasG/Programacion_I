def saludar():
    print("\n\nHola usuario!!\n\n")

def numeros_pares():
    for i in range(10):
        if i%2 == 0:
            print(i)

while True:
    print("-- Menú Interactivo --\n1. Saludar\n2. Mostrar numeros pares\n\n3. Salir")
    opcion=int(input("Seleccione la opción: "))
    
    match opcion:
        case 1:
            saludar()
        case 2:
            numeros_pares()
        case 3:
            break
        case _:
            print("\n\nERROR: Ingrese una opción correcta.\n\n")