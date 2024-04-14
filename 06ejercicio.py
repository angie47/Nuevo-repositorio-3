# Ejercicio 6
#Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
def asignar_grupo(nombre, sexo):
    """Asigna a un usuario a un grupo basado en su nombre y sexo."""
    if sexo == "M":
        return "A" if nombre.lower() < "m" else "B"
    else:
        return "A" if nombre.lower() > "F" else "B"

# Solicita al usuario que ingrese su nombre
nombre_usuario = input("¿Cómo te llamas? ")

# Solicita al usuario que indique su sexo y valida que sea "M" o "H"
sexo_usuario = ""
while sexo_usuario not in ("M", "F"):
    sexo_usuario = input("¿Cuál es tu sexo (M o F)? ")
    if sexo_usuario not in ("M", "H"):
        print("Por favor, ingresa un sexo válido (M o F).")

# Asigna al usuario a un grupo utilizando la función definida y lo imprime
grupo_asignado = asignar_grupo(nombre_usuario, sexo_usuario)
print("Tu grupo es " + grupo_asignado)
