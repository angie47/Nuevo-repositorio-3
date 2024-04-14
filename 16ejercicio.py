# Ejercicio n16

# Solicita al usuario que introduzca la cantidad de barras de pan no frescas vendidas
numero_barras_vendidas = int(input("Introduce el número de barras vendidas que no son frescas: "))

# Precio original de una barra de pan fresca
precio_original = 3.49 

# Descuento aplicado a las barras de pan que no son frescas (60%)
descuento_barras_no_frescas = 0.6

# Calcula el coste total aplicando el descuento a las barras de pan no frescas
coste_total = numero_barras_vendidas * precio_original * (1 - descuento_barras_no_frescas)

# Muestra el precio original de una barra de pan fresca
print("El coste de una barra fresca es " + str(precio_original) + "€")

# Muestra el porcentaje de descuento aplicado a las barras de pan no frescas
print("El descuento sobre una barra no fresca es " + str(descuento_barras_no_frescas * 100) + "%")

# Muestra el coste final a pagar después de aplicar el descuento, redondeado a dos decimales
print("El coste final a pagar es " + str(round(coste_total, 2)) + "€")
