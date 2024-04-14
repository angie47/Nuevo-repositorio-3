# Ejercicio n15
# Definición de la función para calcular la media aritmética de una lista de números
def mean(sample):
    """
    Calcula la media (promedio) de una muestra de números.
    
    Parámetros:
    sample: Es una lista de números (puede contener enteros y/o flotantes).
    
    Devuelve:
    La media de los números en la lista 'sample'.
    """
    # La función sum() suma todos los elementos de la lista 'sample',
    # y len() devuelve la cantidad de elementos en la lista.
    # La división de la suma total por la cantidad de elementos da como resultado la media.
    return sum(sample) / len(sample)

# Ejecución de la función 'mean' con una lista de números enteros y muestra el resultado
print(mean([1, 2, 3, 4, 5]))

# Ejecución de la función 'mean' con una lista de números flotantes y muestra el resultado
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
