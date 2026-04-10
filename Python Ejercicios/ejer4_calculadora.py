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
            print("Por favor ingrese un número válido.")
            print("")
    return a
    
def salidaNumeros(res):
    if res >= 0:
        print(f"La respuesta es: {res:.2f}") #.2f es igual que en C
        time.sleep(2.5) # el parámetro son segundos
        print("")
        print("")
    else:
        print("ERROR.")
        print("Resultado negativo.")
        time.sleep(2.5)

n1=0
n2=0

while True:
    print("-- Calculadora --")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("")
    print("5. Salir")
    print("")
    menu_opcion= int(input("Ingrese la operación a realizar: "))
    
    if menu_opcion == 1:
        n1 = entradaNumero(n1)
        n2= entradaNumero(n2)
        res= n1+n2
        salidaNumeros(res)
    elif menu_opcion == 2:
        n1 = entradaNumero(n1)
        n2= entradaNumero(n2)
        res= n1-n2
        salidaNumeros(res)
    elif menu_opcion == 3:
        n1 = entradaNumero(n1)
        n2= entradaNumero(n2)
        res= n1*n2
        salidaNumeros(res)
    elif menu_opcion == 4:
        n1 = entradaNumero(n1)
        n2= entradaNumero(n2)
        res= n1/n2
        salidaNumeros(res)
    elif menu_opcion == 5:
        break
    else:
        print("ERROR.")
        print("Ingrese una opción válida.")