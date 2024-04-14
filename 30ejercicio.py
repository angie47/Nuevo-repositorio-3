# Ejercicio n30
# Programa que pregunta el correo electrónico del usuario en la consola y muestre por pantalla 

# Función para validar la estructura de un correo electrónico
def validar_email(email):
    return '@' in email and '.' in email.split('@')[1]

# Función para generar un correo institucional a partir de uno personal
def generar_correo_institucional(email, dominio='ceu.es'):
    if validar_email(email):
        usuario = email.split('@')[0]
        return f"{usuario}@{dominio}"
    return "Correo electrónico inválido."

# Solicitar al usuario que ingrese su correo electrónico personal
email_personal = input("Introduce tu correo electrónico personal: ")

# Generar y mostrar el correo institucional
print(generar_correo_institucional(email_personal))
