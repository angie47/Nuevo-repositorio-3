# Ejercicio n25
# Solicita al usuario que ingrese una muestra de números separados por comas
input_str = input("Introduce una muestra de números separados por comas: ")
# Convierte la cadena de entrada en una lista de cadenas numéricas
num_strings = input_str.split(',')
# Convierte la lista de cadenas en una lista de enteros
numbers = [int(num) for num in num_strings]
# Convierte la lista en una tupla
numbers_tuple = tuple(numbers)

# Inicializa las variables para calcular la suma y la suma de cuadrados
total_sum = 0
sum_of_squares = 0

# Calcula la suma y la suma de cuadrados
for num in numbers_tuple:
    total_sum += num
    sum_of_squares += num ** 2

# Calcula la media
mean = total_sum / len(numbers_tuple)
# Calcula la desviación estándar
standard_deviation = (sum_of_squares / len(numbers_tuple) - mean ** 2) ** 0.5
# Imprime la media y la desviación estándar
print(f'La media es {mean}, y la desviación típica es {standard_deviation}')
