import time # Para el time.sleep

def entradaNumero(a):
    while True:
        a=input("Ingrese el número a ser operado: ")
        
        # Try convierte el valor ingresado en float, si
        # es un número entoces sale del bucle, si es un string
        # dará error y volverá a pedir una entrada válida.
        try:
            a = float(a)
            break
        except ValueError:
            print("Por favor ingrese un número válido.\n")
    return a
    
def salidaNumeros(res):
    if res >= 0:
        print(f"La respuesta es: {res:.2f}\n\n") #.2f es igual que en C
        time.sleep(2.5) # el parámetro son segundos
    else:
        print("ERROR.\nResultado negativo.\n")
        time.sleep(2.5)

n1=0
n2=0

while True:
    print("-- Calculadora --\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n\n5. Salir\n")
    menu_opcion= int(input("Ingrese la operación a realizar: "))
    
    match menu_opcion:
        case 1:
            n1 = entradaNumero(n1)
            n2= entradaNumero(n2)
            res= n1+n2
            salidaNumeros(res)
        case 2:
            n1 = entradaNumero(n1)
            n2= entradaNumero(n2)
            res= n1-n2
            salidaNumeros(res)
        case 3:
            n1 = entradaNumero(n1)
            n2= entradaNumero(n2)
            res= n1*n2
            salidaNumeros(res)
        case 4:
            n1 = entradaNumero(n1)
            n2= entradaNumero(n2)
            res= n1/n2
            salidaNumeros(res)
        case 5:
            break
        case _:
            print("ERROR.\nIngrese una opción válida.\n\n")