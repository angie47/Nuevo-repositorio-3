# Ejercicio 7
# Solicita al usuario que ingrese su edad y la convierte en un número entero
edad_usuario = int(input("Introduce tu edad: "))

# Inicializa la variable para almacenar el precio de la entrada
precio_entrada = 0

# Determina el precio de la entrada en función de la edad del usuario
if edad_usuario < 4:
    precio_entrada = 0  # Entrada gratuita para menores de 4 años
elif edad_usuario <= 18:
    precio_entrada = 4  # Precio reducido para usuarios de 4 a 18 años
else:
    precio_entrada = 10  # Precio estándar para usuarios mayores de 18 años

# Muestra el precio de la entrada
print(f"El precio de la entrada es {precio_entrada} €.")
