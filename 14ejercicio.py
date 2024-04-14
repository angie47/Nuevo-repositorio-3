# Ejercicio n14

# Función para saludar al usuario por su nombre
def saludar_usuario(nombre_usuario):
    """
    Saluda al usuario con su nombre.
    
    :param nombre_usuario: str - Nombre del usuario.
    :return: None
    """
    # Imprime un saludo personalizado que incluye el nombre del usuario
    print(f"¡Hola {nombre_usuario}!")

# Solicita al usuario que ingrese su nombre
nombre = input("Introduce tu nombre: ")

# Llama a la función para saludar al usuario con el nombre ingresado
saludar_usuario(nombre)
