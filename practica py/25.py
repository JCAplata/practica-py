# Creamos una lista vacía para almacenar las palabras
palabras = []
# Solicitamos al usuario que ingrese 5 palabras
print('Ingresa 5 palabras')
for i in range(1, 6):
    # Convertimos la palabra ingresada a mayúsculas
    palabra = input(f'Ingresa la palabra {i}: ').upper()
    # Verificamos si la palabra contiene solo letras
    if palabra.isalpha():
        palabras.append(palabra)
    else:
        print('La palabra no puede contener numeros')
        break
# Mostramos la lista de palabras ingresadas
print(f'Lista de palabras: {palabras}')
# Ordenamos la lista en orden alfabético
palabras.sort()
print(f'Lista de palabras ordenada en orden alfabetico: {palabras}')
# Solicitamos una palabra para remover de la lista
remover = input('Ingresa una palabra de la lista a remover: ').upper()
# Verificamos si la palabra está en la lista y la eliminamos si existe
if remover in palabras:
    palabras.remove(remover)
    print(palabras)
else:
    print('La palabra no existe en la lista')
