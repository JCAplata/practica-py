# Creamos una lista vacía para almacenar los números pares
lista = []
# Solicitamos al usuario que introduzca tres números pares
print('Introduce 3 numeros pares')
# Bucle infinito para capturar los números
while True:
    try:
        # Solicitamos al usuario un número entero
        numero = int(input('Escribe un numero par: '))
    except ValueError:
        # Si el valor introducido no es un número entero, mostramos un mensaje de error
        print('Error, no es un numero valido')
    else:
        # Verificamos si el número es par
        if numero % 2 == 0:
            # Agregamos el número par a la lista
            lista.append(numero)
            # Si hemos recopilado tres números pares, terminamos el proceso
            if len(lista) == 3:
                print('Lista terminada')
                print(lista)
                break
        else:
            # Si el número no es par, solicitamos otro intento
            print('El numero no es par, intenta nuevamente')

