# Ejercicio n11
def calcular_interes_compuesto(monto_inicial, tasa_interes, periodo_años):
    """
    Calcula el capital final utilizando la fórmula del interés compuesto.
    :param monto_inicial: Cantidad de dinero inicial a invertir.
    :param tasa_interes: Interés porcentual anual.
    :param periodo_años: Número de años de la inversión.
    :return: El capital final redondeado a dos decimales.
    """
    capital_final = monto_inicial * (tasa_interes / 100 + 1) ** periodo_años
    return round(capital_final, 2)

# Solicita al usuario la cantidad de dinero a invertir
monto_inicial = float(input("¿Cantidad a invertir? "))
# Solicita al usuario el interés porcentual anual
tasa_interes = float(input("¿Interés porcentual anual? "))
# Solicita al usuario el número de años que durará la inversión
periodo_años = int(input("¿Años?"))

# Calcula el capital final utilizando la función definida
capital_final = calcular_interes_compuesto(monto_inicial, tasa_interes, periodo_años)

# Muestra el capital final
print(f"Capital final: {capital_final}")
