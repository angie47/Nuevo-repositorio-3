# Ejercicio n28
# Definición de la función factorial
def factorial(n):
    """
    Calcula el factorial de un número entero positivo.
    
    Parámetros:
    n: Es un entero positivo.
    
    Devuelve:
    El factorial de n.
    """
    # Inicializa una variable temporal para almacenar el resultado
    resultado = 1
    
    # Bucle que multiplica resultado por cada número de 1 a n
    for i in range(1, n + 1):
        resultado *= i
    
    # Devuelve el resultado calculado
    return resultado

# Ejemplos de uso de la función factorial
print(factorial(4))  # Debería imprimir 24, ya que 4! = 4 * 3 * 2 * 1 = 24
print(factorial(20)) # Debería imprimir 2432902008176640000, que es 20!

