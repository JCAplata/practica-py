listaOriginal = [1, 2, 3, 4, 5]  # Lista original con números
# Se crea una copia de la lista original
listaCopia = listaOriginal.copy()
try:
    # Solicita un número al usuario para agregar a la lista original
    numero = int(input('Escribe un nuevo numero para añadir a la lista: '))
    listaOriginal.append(numero)  # Agrega el número a la lista original
except(ValueError):
    print('Tiene que ser un numero')  # Mensaje de error si la entrada no es un número
else:
    # Muestra ambas listas después de la modificación
    print(f'La original: {listaOriginal}')
    print(f'La copia: {listaCopia}')
