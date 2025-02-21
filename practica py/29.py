# Definimos una lista con nombres repetidos
lista = ['camilo', 'juan', 'amezquita', 'carrera', 'juan', 'camilo', 'amezquita', 'carrera', 'carrera', 'amezquita', 'camilo', 'juan']
# Creamos una lista vacía para almacenar los índices encontrados
indices_encontrados = []
# Mostramos la lista original
print(lista)
# Solicitamos al usuario una palabra para buscar en la lista
palabra = input('Escoge una palabra que desees guardar: ')
# Verificamos si la palabra está en la lista
if palabra in lista:
    # Iteramos sobre la lista y almacenamos las coincidencias
    for i in lista:
        if i == palabra:
            indices_encontrados.append(i)
        else:
            pass
else:
    print('La palabra no esta en la lista')
# Mostramos las coincidencias encontradas
print(f'Palabras encontradas en la lista: {indices_encontrados}')