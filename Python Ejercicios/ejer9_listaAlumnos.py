def calcular_promedio(alumnos):
    return sum(alumnos) / len(alumnos)

def nota_maxima_lista(alumnos):
    return max(alumnos)

def nota_minima_lista(alumnos):
    return min(alumnos)

def cantidad_alumnos_aprobados(alumnos):
    aprobados = 0
    for nota in alumnos:
        if nota >= 6:
            aprobados += 1
    return aprobados, len(alumnos)

alumnos=[10, 5.9, 6, 5, 8, 7.75, 4]

print(f"Promedio de notas: {calcular_promedio(alumnos): .2f}")
print("Nota maxima: ", nota_maxima_lista(alumnos))
print("Nota minima: ", nota_minima_lista(alumnos))
a,b = cantidad_alumnos_aprobados(alumnos)
print(f"Cantidad de alumnos aprobados: {a} de {b}")