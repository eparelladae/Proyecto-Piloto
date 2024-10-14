# Solicitar una frase al usuario
frase = str(input("Introduce una frase: ")).lower()

# Inicializar un diccionario para contar las vocales
conteo_vocales = {}

# Definir las vocales
vocales = "aeiou"

# Contar las vocales en la frase
for letra in frase:
    if letra in vocales:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
        else:
            conteo_vocales[letra] = 1

# Mostrar el resultado
print("Conteo de vocales:", conteo_vocales)
