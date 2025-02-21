frutas = ["manzana", "pera", "manzana", "naranja", "manzana"]  # Lista de frutas
# Solicita al usuario una fruta para buscar en la lista
fruta = input('Ingrese la fruta que quiere buscar: ').lower()
if fruta.isalpha():  # Verifica que la entrada solo contenga letras
    if frutas.count(fruta) > 0:  # Comprueba si la fruta está en la lista y cuántas veces aparece
        print(f'La fruta aparece: {frutas.count(fruta)} veces')  # Muestra la cantidad de veces que aparece la fruta
    else:
        print('La fruta no está en la lista')  # Mensaje si la fruta no está en la lista
else:
    print('¿Cuándo has visto una fruta con números?')  # Mensaje de error si la entrada no es válida