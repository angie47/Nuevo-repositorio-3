# Ejercicio n27
# Función para imprimir una lista en orden inverso

def imprimir_inverso(lista_numeros):
    """
    Imprime los elementos de una lista en orden inverso, separados por comas.
    
    Parámetros:
    lista_numeros: La lista de números a imprimir en orden inverso.
    """
    # Bucle que recorre la lista en orden inverso utilizando índices negativos
    for i in range(1, len(lista_numeros) + 1):
        # Imprime el número actual seguido de una coma y un espacio
        print(lista_numeros[-i], end=", ")

# Lista de números del 1 al 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Llama a la función para imprimir la lista en orden inverso
imprimir_inverso(numbers)
