# Ejercicio n18
# Definición de la función para calcular el índice de masa corporal (IMC)
def calcular_imc(peso_kg, estatura_m):
    """
    Calcula el IMC utilizando la fórmula IMC = peso (kg) / estatura (m)^2.
    
    Parámetros:
    peso_kg: Peso de la persona en kilogramos.
    estatura_m: Estatura de la persona en metros.
    
    Devuelve:
    El IMC de la persona.
    """
    # Calcula el IMC y lo redondea a dos decimales
    return round(peso_kg / estatura_m**2, 2)

# Solicita al usuario que introduzca su peso en kilogramos y lo convierte a tipo float
peso_usuario = float(input("¿Cuál es tu peso en kg? "))
# Solicita al usuario que introduzca su estatura en metros y lo convierte a tipo float
estatura_usuario = float(input("¿Cuál es tu estatura en metros?"))
imc_usuario = calcular_imc(peso_usuario, estatura_usuario)
# Muestra el IMC del usuario concatenando el resultado con un mensaje
print("Tu índice de masa corporal es " + str(imc_usuario))
    