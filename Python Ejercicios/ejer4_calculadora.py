import time # Para el time.sleep

def entradaNumeros(a,b):
    a= float(input("Ingrese el primer número: "))
    b= float(input("Ingrese el segundo número: "))
    return a, b
    
def salidaNumeros(res):
    if res >= 0:
        print(f"La respuesta es: {res:.2f}") #.2f es igual que en C
        time.sleep(2.5) # el parámetro son segundos
        print("")
        print("")
    else:
        print("ERROR.")
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
        n1, n2 = entradaNumeros(n1,n2)
        res= n1+n2
        salidaNumeros(res)
    elif menu_opcion == 2:
        n1, n2 = entradaNumeros(n1,n2)
        res= n1-n2
        salidaNumeros(res)
    elif menu_opcion == 3:
        n1, n2 = entradaNumeros(n1,n2)
        res= n1*n2
        salidaNumeros(res)
    elif menu_opcion == 4:
        n1, n2 = entradaNumeros(n1,n2)
        res= n1/n2
        salidaNumeros(res)
    elif menu_opcion > 5:
        print("ERROR.")
        print("Ingrese una opción válida.")
    elif menu_opcion == 5:
        break