# Esta función solicita al usuario que ingrese su edad y la devuelve como un entero.
def solicitar_edad():
    return int(input("¿Cuál es tu edad? "))

# Esta función recibe una edad y determina si es menor o mayor de edad, imprimiendo el resultado.
def determinar_mayoria_edad(edad):
    if edad < 18:
        print("Eres menor de edad.")
    else:
        print("Eres mayor de edad.")

# Programa principal
# Solicitamos la edad del usuario.
edad_usuario = solicitar_edad()

# Determinamos si el usuario es menor o mayor de edad e imprimimos el resultado.
determinar_mayoria_edad(edad_usuario)

