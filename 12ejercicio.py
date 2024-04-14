# Ejercicio 12
# Función para calcular el interés compuesto
def calcular_capital_final(monto_inicial, tasa_interes, tiempo_años):
    """
    Calcula el capital final con interés compuesto.
    
    :param monto_inicial: float - Cantidad de dinero inicial a invertir.
    :param tasa_interes: float - Tasa de interés anual en porcentaje.
    :param tiempo_años: int - Cantidad de años de la inversión.
    :return: float - Capital final redondeado a dos decimales.
    """
    # Aplica la fórmula del interés compuesto
    capital = monto_inicial * ((tasa_interes / 100) + 1) ** tiempo_años
    # Redondea el resultado a dos decimales
    return round(capital, 2)

# Solicita al usuario los datos necesarios para la inversión
monto_inicial = float(input("¿Cantidad a invertir? "))
tasa_interes = float(input("¿Interés porcentual anual? "))
tiempo_años = int(input("¿Años?"))
# Llama a la función para calcular el capital final
capital_final = calcular_capital_final(monto_inicial, tasa_interes, tiempo_años)
# Muestra el resultado al usuario
print(f"Capital final: {capital_final}")
