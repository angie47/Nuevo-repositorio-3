# Ejercicio n26

# Lista vacía para almacenar los números ganadores
winning_numbers = []

# Bucle para solicitar al usuario que ingrese seis números ganadores
for i in range(6):
    # Solicita al usuario que ingrese un número ganador y lo agrega a la lista
    number = int(input("Introduce un número ganador: "))
    winning_numbers.append(number)

# Ordena la lista de números ganadores
winning_numbers.sort()

# Convierte la lista de números ganadores a una cadena y la imprime
print("Los números ganadores son " + str(winning_numbers))
