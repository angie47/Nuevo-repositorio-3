# Ejercicio n13
# Programa que calcula el peso total de un paquete que se va a enviar, basado en el número de payasos y muñecas que contiene.

# Peso de un payaso en gramos
peso_por_payaso = 112

# Peso de una muñeca en gramos
peso_por_muñeca = 75

# Solicita al usuario la cantidad de payasos a enviar
cantidad_payasos = int(input("Introduce el número de payasos a enviar: "))

# Solicita al usuario la cantidad de muñecas a enviar
cantidad_muñecas = int(input("Introduce el número de muñecas a enviar: "))

# Calcula el peso total del paquete sumando el peso de los payasos y las muñecas
peso_total_paquete = (peso_por_payaso * cantidad_payasos) + (peso_por_muñeca * cantidad_muñecas)

# Muestra el peso total del paquete
print(f"El peso total del paquete es {peso_total_paquete}")
