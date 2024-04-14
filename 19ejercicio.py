# Ejercicio n19

# Solicita al usuario su edad y la convierte a un número entero
edad_usuario = int(input("¿Cuántos años tienes? "))

# Itera a través de cada año de vida del usuario y muestra un mensaje
for anio in range(1, edad_usuario + 1):
    print(f"Has cumplido {anio} años")
