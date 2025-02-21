# Definimos una lista de números del 1 al 10
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Inicializamos las variables para almacenar el máximo y mínimo
numeroMax = 0
numeroMin = 1000
# Iteramos sobre la lista para encontrar el mayor y el menor número
for i in lista:
    # Si el número actual es mayor que numeroMax, lo actualizamos
    if i > numeroMax:
        numeroMax = i
    else:
        pass
    # Si el número actual es menor que numeroMin, lo actualizamos
    if i < numeroMin:
        numeroMin = i
    else:
        pass
# Imprimimos el número máximo encontrado
print(numeroMax)
# Imprimimos el número mínimo encontrado
print(numeroMin)
# Calculamos e imprimimos el promedio de la lista
print(sum(lista)/len(lista))