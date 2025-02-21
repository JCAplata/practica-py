# Definimos una lista de números del 1 al 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Creamos listas vacías para almacenar los números pares e impares
pares = []
impares = []
# Iteramos sobre cada número en la lista
for x in lista:
    # Si el número es divisible por 2, es par y lo añadimos a la lista de pares
    if x % 2 == 0:
        pares.append(x)
    # Si no es divisible por 2, es impar y lo añadimos a la lista de impares
    else:
        impares.append(x)
# Imprimimos la lista original
print(f'La lista es: {lista}')
# Imprimimos los números pares encontrados
print(f'Los pares son: {pares}')
# Imprimimos los números impares encontrados
print(f'Los impares son: {impares}')

