# Ejercicio n20
# Solicita al usuario la cantidad inicial a invertir
capital_inicial = float(input("¿Cantidad a invertir? "))

# Solicita al usuario el interés anual en porcentaje
tasa_interes = float(input("¿Interés porcentual anual? "))

# Solicita al usuario la duración de la inversión en años
duracion_inversion = int(input("¿Años?"))

# Realiza el cálculo de la inversión para cada año
for anio in range(duracion_inversion):
    # Calcula el capital acumulado aplicando el interés anual
    capital_inicial *= 1 + tasa_interes / 100
    
    # Imprime el capital acumulado al final de cada año, redondeado a dos decimales
    print(f"Capital tras {anio + 1} años: {round(capital_inicial, 2)}")
