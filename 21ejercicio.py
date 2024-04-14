# Ejercicio n21
# Programa que lee las tblas del 1 al 10

# Imprime el encabezado de la tabla
print("Tabla de Multiplicar del 1 al 10")
print("-" * 61)  # Imprime una línea separadora

# Imprime los encabezados de las columnas
print("\t", end="")
for encabezado in range(1, 11):
    print(encabezado, end="\t")
print("\n" + "-" * 61)  # Imprime una línea separadora y un salto de línea

# Imprime la tabla de multiplicar con encabezados de fila
for multiplicando in range(1, 11):
    # Imprime el encabezado de la fila actual
    print(multiplicando, end="\t")
    
    # Itera a través de cada multiplicador para la fila actual
    for multiplicador in range(1, 11):
        # Calcula el producto y lo imprime
        print(multiplicando * multiplicador, end="\t")
    
    # Imprime un salto de línea para comenzar una nueva fila
    print("\n" + "-" * 61)
