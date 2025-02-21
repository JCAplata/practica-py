def evaluarEstado(nota) -> int:
    """
    Función que evalúa el estado de un estudiante según su nota.
    La nota debe estar en el rango de 1 a 10.
    """
    try:
        nota = int(input('Ingresa la nota (de 1 a 10): '))
        if nota > 10 or nota < 0:
            print('La nota no es válida')
        else:
            match nota:
                case 10:
                    print('Excelente')
                case 9 | 8:
                    print('Muy bien')
                case 7 | 6:
                    print('Bien')
                case 5 | 4:
                    print('Regular')
                case _:
                    print('Reprobado')
    except ValueError:
        print('No es una nota válida')
nota = ()  # Variable inicializada
evaluarEstado(nota)


