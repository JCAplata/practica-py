numeros = [3, 8, 1, 7, 2]  # Lista de números desordenados
# Solicita al usuario el orden de organización de la lista
orden = input('¿Desea organizar los numeros de manera ascendente o descendente?(ascendente o descendente): ')
if orden.lower() == 'ascendente':  # Verifica si el usuario eligió orden ascendente
    numeros.sort()  # Ordena la lista de forma ascendente
    print(f'La lista queda asi: {numeros}')  # Muestra la lista ordenada
elif orden.lower() == 'descendente':  # Verifica si el usuario eligió orden descendente
    numeros.sort(reverse=True)  # Ordena la lista de forma descendente
    print(f'La lista queda asi: {numeros}')  # Muestra la lista ordenada
else:
    print('Elija una de las opciones dadas')  # Mensaje si la opción ingresada no es válida
