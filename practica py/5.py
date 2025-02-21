numeros = [1, 2, 3, 4, 5]  # Lista inicial de números
# Bucle infinito para manejar el menú de opciones
while True:
    try:
        # Solicita al usuario una opción del menú
        menu = int(input('Menu:\n 1. Hacer pop sin indice.\n 2. Hacer pop con indice.\n 3. Salir\nEscribe tu seleccion: '))
    except(ValueError):
        # Captura error si la entrada no es un número válido
        print('Escribe un numero valido (1, 2 o 3)')
    else:
        match menu:
            case 1:
                # Elimina el último elemento de la lista
                elementoBorrar = numeros.pop()
                print(f'El elemento que se borro fue: {elementoBorrar}')
                print(f'La lista quedo de esta manera: {numeros}')
            case 2:
                try:
                    # Muestra la lista actual
                    print(numeros)
                    # Solicita al usuario el índice a eliminar
                    indice = int(input('que posicion deseas borrar: '))
                except (ValueError):
                    # Captura error si la entrada no es un número válido
                    print('Ingresa un numero valido')
                else:
                    try:
                        # Elimina el elemento en la posición indicada
                        elementoBorrar = numeros.pop(indice-1)
                    except (IndexError):
                        # Captura error si el índice está fuera de rango
                        print('Esa posicion no se encuentra en la lista')
                    else:
                        print(f'El elemento que se borro es: {elementoBorrar}')
                        print(f'La lista quedo asi: {numeros}') 
            case 3:
                # Opción para salir del programa
                print('Cerrando el programa...')
                break
            case _:
                # Mensaje si el usuario ingresa una opción inválida
                print('El numero no esta dentro de las opciones, introduzca una opcion valida: ')

