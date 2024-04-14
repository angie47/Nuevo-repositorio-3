# Ejercicio 5
# Solicita al usuario que ingrese su edad y la convierte a un número entero

age = int(input("¿Cuál es tu edad? "))

# Solicita al usuario que ingrese sus ingresos mensuales y los convierte a un número flotante
income = float(input("¿Cuales son tus ingresos mensuales?"))

# Comprueba si la edad del usuario es menor o igual a 16 o si sus ingresos son menos de 1000
if age <= 16 or income < 1000:
    # Si se cumple alguna de las condiciones anteriores, se imprime que el usuario no tiene que cotizar
    print("No tienes que cotizar")
else:
    # Si no se cumplen las condiciones, se imprime que el usuario tiene que cotizar
    print("Tienes que cotizar")
