# Ejercicio n23
# Programa que muestra el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

# Bucle infinito para solicitar entrada del usuario
while True:
    # Solicita al usuario que ingrese texto
    frase = input("Introduce algo (o escribe 'salir' para finalizar): ")
    
    # Verifica si el usuario ingresó la palabra 'salir'
    if frase.lower() == "salir":  # .lower() asegura que funcione para 'SALIR', 'Salir', etc.
        print("Saliendo del programa...")
        break  # Interrumpe el bucle y termina el programa
    
    # Imprime lo que el usuario ingresó
    print("Escribiste:", frase)

# Aquí termina el bucle y el programa
