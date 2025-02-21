# Creamos una lista vacía para almacenar los números
lista = []
# Iteramos del 1 al 10
for i in range(1, 11):
    # Si el número es 5, lo omitimos y continuamos con la siguiente iteración
    if i == 5:
        continue
    # Si el número es 8, rompemos el bucle y salimos
    if i == 8:
        break
    else:
        # Agregamos el número a la lista
        lista.append(i)
# Imprimimos la lista resultante
print(lista)