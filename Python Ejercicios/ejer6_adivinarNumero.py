import random

num_random = random.randint(1,100)
print("\nLa maquina ha decidido un numero aleatorio del 1 al 100\n")

for i in range(7):
    num_usuario = int(input(f"\nIntento {i+1}, Ingrese un numero: \n"))
    
    if num_usuario==num_random:
        print(f"Felicidades! El numero {num_usuario} fue el elegido por la maquina.")
        break
    elif num_usuario<num_random:
        print("Su numero ingresado es MENOR al de la maquina.")
    else:
        print("Su numero ingresado es MAYOR al de la maquina.")
else:
    print(f"\nHa fallado los 7 intentos, el numero elegido por la maquina fue {num_random}.\n")