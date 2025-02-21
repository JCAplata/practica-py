# Definimos dos listas con nombres de series de televisión
lista1 = ['marvel', 'harrypoter', 'rapidosfueriosos', 'the walking dead']
lista2 = ['La Casa de Papel', 'El Juego del Calamar', 'cobra kai']
# Solicitamos al usuario si desea unir las listas
SiNo = input('¿Deseas unir la listas? (si o no): ').lower()
# Verificamos si la entrada es solo alfabética
if SiNo.isalpha():
    # Si la respuesta es 'si', unimos ambas listas y las mostramos
    if SiNo == 'si':
        lista1.extend(lista2)
        print(f'La lista es: {lista1}')
    # Si la respuesta es 'no', mostramos ambas listas por separado
    elif SiNo == 'no':
        print(f'La lista 1 es: {lista1}')
        print(f'La lista 2 es: {lista2}')
    # Si la respuesta no es 'si' o 'no', mostramos un mensaje de error
    else:
        print('La eleccion no es valida')
else:
    # Mensaje de error si la entrada contiene números u otros caracteres no alfabéticos
    print('La eleccion no es valida, no puede ser un numero')
