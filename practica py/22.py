# Definimos una función para sumar dos números flotantes y mostrar el resultado
def suma(a : float, b : float):
    print(f'La suma es: {a + b}')
# Bucle infinito para permitir múltiples sumas
while True:
    try:
        # Solicitamos al usuario el primer número y convertimos a float
        a = float(input('Escribe el primer numero a sumar: '))
    except ValueError:
        # Si la conversión falla, mostramos un mensaje de error
        print('no es un numero valido')
    else:
        pass
    try:
        # Solicitamos al usuario el segundo número y convertimos a float
        b = float(input('Escribe el segundo numero a sumar: '))
    except ValueError:
        # Si la conversión falla, mostramos un mensaje de error
        print('Ese no es un numero valido')
    else:
        # Llamamos a la función de suma con los valores ingresados
        suma(a, b)
        # Preguntamos al usuario si desea realizar otra suma
        repetir = input('¿Deseas volver a hacer otra suma? s/n: ').lower()
        if repetir == 'n' or repetir == 'no':
            # Si el usuario elige 'n' o 'no', terminamos el programa
            print('Programa finalizado... ')
            break
        else:
            pass


