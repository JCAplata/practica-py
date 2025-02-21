numeros = [1, 2, 3]
numeros2 = []
print('Escribe tres numeros')
# Bucle para solicitar tres números al usuario
for i in range(1, 4):
    try:
        # Solicita al usuario un número entero
        numero = int(input(f'Escribe el numero {i}: '))
    except (ValueError):
        # Captura error si el usuario no ingresa un número entero
        print('numero entero por favor')
        break
    else:
        # Agrega el número ingresado a la lista numeros2
        numeros2.append(numero)
    if i == 3:
        # Mensaje de finalización
        print('finalizada')
        # Extiende la lista numeros con los valores ingresados
        numeros.extend(numeros2)
        # Muestra la lista final de números
        print(f'tus numeros son: {numeros}')
