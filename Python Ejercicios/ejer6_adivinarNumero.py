import random

bandera=False
num_random = random.randint(1,100)
print("\nLa maquina ha decidido un numero aleatorio del 1 al 100\n")

for i in range(7):
    num_usuario = int(input(f"\nIntento {i+1}, Ingrese un numero: \n"))
    
    if num_usuario>num_random:
        print("Su numero ingresado es MAYOR al de la maquina.")
    elif num_usuario<num_random:
        print("Su numero ingresado es MENOR al de la maquina.")
    else:
        bandera=True
        break

#se puede poner un else al for, probar poniendo primero la condicion igual, luego menor y ultimo mayor
if bandera==True:
        print(f"Felicidades! El numero {num_usuario} fue el elegido por la maquina.")
else:
    print(f"Ha fallado los 7 intentos, el numero elegido por la maquina fue {num_random}.")