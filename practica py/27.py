calificacion = []
while True:
    try:
        numero = int(input('Escriba una calificacion de 0 a 5 (Para finalizar ingrese un valor negativo): '))
    except ValueError:
        print('No es un numero valido, ingrese otro')
    else:
        if numero in [1, 2, 3, 4, 5]:
            calificacion.append(numero)
        if numero > 5:
            print('Esa nota no es valida')
        if numero < 0:
            print('Ejecucion finalizada')
            break
print(f'Las calificaciones fueron: {calificacion}')
print(f'El promedio de las calificaciones es: {sum(calificacion)/len(calificacion)}')