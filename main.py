# Solicitar una frase al usuario
frase = str(input("Introduce una frase: ")).lower()

# Inicializar un diccionario para contar las vocales y otro para contar las consonantes
conteo_vocales = {}
conteo_consonantes = {}

# Definir las vocales
vocales = "aeiou"

# Contar las vocales y consonantes en la frase
for letra in frase:
    if letra != " ":
        if letra in vocales:
            if letra in conteo_vocales:
                conteo_vocales[letra] += 1
            else:
                conteo_vocales[letra] = 1
        else:
            if letra in conteo_consonantes:
                conteo_consonantes[letra] +=1
            else:
                conteo_consonantes[letra] = 1

# Mostrar el resultado
print("Conteo de vocales:", conteo_vocales)
print("Conteo de consonantes:", conteo_consonantes)
