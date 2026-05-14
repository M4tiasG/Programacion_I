def suma(a, b):
    return a + b

retorno1 = suma(2, 3)
assert retorno1 == 5, "Error: La suma no es correcta"
print(retorno1)

retorno2 = suma(-1, 1)
print(retorno2)
assert retorno2 == 0, "Error: La suma no es correcta"

retorno3 = suma(0, 0)
print(retorno3)
assert retorno3 >= 0, "Error: La suma da un resultado negativo"