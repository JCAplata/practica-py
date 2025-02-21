animales = ['perro', 'gato', 'elefante', 'tigre']  # Lista inicial de animales
# Bucle infinito para solicitar al usuario un animal a eliminar
while True:
    animal = input('Escribe el animal que quieres eliminar: ')
    if animal.isalpha():  # Verifica que la entrada solo contenga letras
        if animal.lower() in animales:  # Verifica si el animal está en la lista
            animales.remove(animal.lower())  # Elimina el animal de la lista
            print(animales)  # Muestra la lista actualizada
            break  # Sale del bucle
        else:
            print('El animal no esta en la lista, ingresa uno nuevo')  # Mensaje de error si el animal no está en la lista
    else:
        print('Escribe un animal valido (Sin numeros o caracteres especiales)')  # Mensaje de error si la entrada no es válida
