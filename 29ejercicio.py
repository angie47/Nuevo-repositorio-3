# Ejercicio n29

# Preguntar al usuario por la renta anual
ingreso_anual = float(input("¿Cuál es tu ingreso anual? "))

# Condicional para determinar el porcentaje de impuestos dependiendo de la renta
if ingreso_anual < 10000:
    porcentaje_impuesto = 5
elif ingreso_anual < 20000:
    porcentaje_impuesto = 15
elif ingreso_anual < 35000:
    porcentaje_impuesto = 20
elif ingreso_anual < 60000:
    porcentaje_impuesto = 30
else:
    porcentaje_impuesto = 45

# Calcular la cantidad de impuestos a pagar
impuestos_a_pagar = ingreso_anual * porcentaje_impuesto / 100

# Mostrar por pantalla la cantidad de impuestos a pagar
print(f"Tienes que pagar {impuestos_a_pagar}€ en impuestos.")
