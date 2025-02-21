colores = ["rojo", "azul", "verde", "amarillo", "negro"]  # Lista de colores disponibles
# Solicita al usuario un color para buscar en la lista
color = input('Ingresa el color que deseas buscar: ').lower()
if color.isalpha():  # Verifica que la entrada solo contenga letras
    if color.lower() in colores:  # Comprueba si el color está en la lista
        print(colores.index(color))  # Imprime la posición del color en la lista
    else:
        print('El color no se encuentra en la lista')  # Mensaje si el color no está en la lista
else:
    print('Es un color, no matemáticas')  # Mensaje de error si la entrada no es válida