def palabras_comunes(parrafo1, parrafo2):
    return parrafo1.intersection(parrafo2)

def palabras_unicas(parrafo1, parrafo2):
    return parrafo1.union(parrafo2)

def palabras_totales(parrafo1, parrafo2):
    return set.union(parrafo1, parrafo2)



parrafo1= "Pyhton es un lenguaje de programacion facil"
parrafo2={"usa", "Python", "web", "para", "se", "poderoso", "es"}

print("Palabras comunes: ", palabras_comunes(parrafo1, parrafo2))
print("Palabras unicas: ", palabras_unicas(parrafo1, parrafo2))
print("Palabras: ", palabras_totales(parrafo1, parrafo2))