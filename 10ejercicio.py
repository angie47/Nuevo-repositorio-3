# Ejercicio n10
# Solicita al usuario que ingrese la cantidad de horas trabajadas
horas_trabajadas = float(input("Introduce tus horas de trabajo: "))

# Solicita al usuario que ingrese la tarifa de pago por hora
tarifa_hora = float(input("Introduce lo que cobras por hora: "))

# Calcula la paga total multiplicando las horas trabajadas por la tarifa por hora
paga_total = horas_trabajadas * tarifa_hora

# Muestra la paga total al usuario
print(f"Tu paga es {paga_total}")
