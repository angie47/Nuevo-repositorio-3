# Ejercicio n22
# Función para contar la ocurrencia de una letra específica en una frase
def contar_letra_en_frase(frase, letra):
    """
    Cuenta cuántas veces aparece una letra en una frase.
    
    Parámetros:
    frase: La frase en la que se buscará la letra.
    letra: La letra que se contará en la frase.
    
    Devuelve:
    El número de veces que la letra aparece en la frase.
    """
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

frase_usuario = input("Introduce una frase: ")
letra_usuario = input("Introduce una letra: ")
ocurrencias = contar_letra_en_frase(frase_usuario, letra_usuario)

# Imprime el resultado utilizando el método format para una mejor legibilidad
print("La letra '{}' aparece {} veces en la frase '{}'.".format(letra_usuario, ocurrencias, frase_usuario))
