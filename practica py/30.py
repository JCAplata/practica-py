# Definimos una lista de números del 1 al 10
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Función que recibe una lista y realiza cálculos en base a la misma
def suma_lista(lista):
    # Verificamos si la lista está vacía
    if len(lista) == 0:
        print('La lista esta vacia')
    else:
        # Iteramos sobre los elementos de la lista
        for i in lista:
            # Si el número es 2, detenemos el bucle
            if i == 2:
                break
            else:
                print(f'El primer numero de la lista es: {i}')
                print(f'La suma del primer numero y la lista es: {sum(lista) + i}')
# Llamamos a la función con la lista definida
suma_lista(lista_numeros)
# Imprimimos la suma total de la lista
print(f'La suma de la lista es: {sum(lista_numeros)}')