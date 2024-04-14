# Ejercio n3
# Esta función solicita al usuario que ingrese un número y lo devuelve como un flotante.
def solicitar_numero(mensaje):
    return float(input(mensaje))

# Esta función realiza la división del dividendo por el divisor y muestra el resultado.
# Si el divisor es cero, muestra un mensaje de error.
def dividir(dividendo, divisor):
    if divisor == 0:
        print("¡Error! No se puede dividir por 0.")
    else:
        print(dividendo / divisor)

# Programa principal
# Solicitamos al usuario que ingrese el dividendo.
dividendo = solicitar_numero("Introduce el dividendo: ")

# Solicitamos al usuario que ingrese el divisor.
divisor = solicitar_numero("Introduce el divisor: ")

# Realizamos la operación de división y mostramos el resultado o un mensaje de error.
dividir(dividendo, divisor)
