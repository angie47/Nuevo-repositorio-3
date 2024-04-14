# Ejercicio n4
# Esta función solicita al usuario que ingrese un número entero y lo devuelve.
def solicitar_numero():
    return int(input("Introduce un número entero: "))

# Esta función determina si un número es par o impar e imprime el resultado.
def determinar_paridad(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")

# Programa principal
# Solicitamos al usuario que ingrese un número entero.
numero = solicitar_numero()

# Determinamos si el número es par o impar e imprimimos el resultado.
determinar_paridad(numero)
