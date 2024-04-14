# Esta función solicita al usuario que ingrese una contraseña y la devuelve.
def solicitar_contraseña():
    return input("Introduce la contraseña: ")

# Esta función recibe la contraseña ingresada y la contraseña clave, y verifica si coinciden.
def verificar_contraseña(contraseña_ingresada, contraseña_clave):
    if contraseña_ingresada.lower() == contraseña_clave:
        print("La contraseña coincide.")
    else:
        print("La contraseña no coincide.")

# Programa principal
# La contraseña clave que se desea verificar.
contraseña_clave = "contraseña"

# Solicitamos al usuario que ingrese una contraseña.
contraseña_usuario = solicitar_contraseña()

# Verificamos si la contraseña ingresada coincide con la clave.
verificar_contraseña(contraseña_usuario, contraseña_clave)
