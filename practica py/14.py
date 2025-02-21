numeros = []  # Lista principal donde se almacenarán los números ingresados
pares = []  # Lista para almacenar los números pares
impares = []  # Lista para almacenar los números impares
def clasificarLista(lista, listaPares, listaImpares):
    """Función para clasificar los números ingresados en pares e impares."""
    for i in range(1, 6):  # Se solicita al usuario ingresar 5 números
        try:
            numero = int(input(f'Escribe el numero {i}/5: '))  # Solicita un número entero al usuario
        except(ValueError):
            print('Ese no es un número')  # Mensaje de error si la entrada no es válida
            break
        else:
            lista.append(numero)  # Agrega el número a la lista principal
        if numero % 2 == 0:
            listaPares.append(numero)  # Si el número es par, se agrega a la lista de pares
        else:
            listaImpares.append(numero)  # Si el número es impar, se agrega a la lista de impares
    # Muestra las listas resultantes
    print(f'La lista quedó así: {lista}\nLos números pares son: {listaPares}\nLos números impares son: {listaImpares}')
# Llamado a la función para ejecutar la clasificación
clasificarLista(numeros, pares, impares)