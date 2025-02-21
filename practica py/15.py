try:
    # Solicita al usuario que ingrese un número entero
    opcion = int(input('Ingrese un valor ENTERO: '))
except (ValueError, NameError):
    # Captura errores si la entrada no es un número entero
    print('Debes ingresar solo NUMEROS ENTEROS')
else:
    # Utiliza match para manejar las opciones ingresadas
    match opcion:
        case 1:
            print('Seleccionaste la opción 1')
        case 2:
            print('Seleccionaste la opción 2')
        case _:
            print('Selección inválida')

