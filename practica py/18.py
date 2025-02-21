nombresPersonas = []

def buscar_personas(lista: list):
    """
    Función para buscar un nombre en la lista de personas.
    """
    nombre = input('Nombre de la persona que quieres buscar: ').lower()
    for x in lista:
        if x == nombre:
            print(f'El nombre de {nombre} sí se encuentra en la lista')
            break
    else:
        print('El nombre no fue encontrado en la lista')

menu = """
----------------
---- MENU -----
----------------
1. AGREGAR NOMBRE
2. VER NOMBRES
3. BUSCAR NOMBRE
4. SALIR
"""

while True:
    print(menu)
    try:
        option = int(input('Escribe tu selección: '))
    except ValueError:
        print('No es una opción válida')
    else:
        match option:
            case 1:
                nombre = input('Escribe el nombre de una persona: ').lower()
                nombresPersonas.append(nombre)
            case 2:
                print(nombresPersonas)
            case 3:
                buscar_personas(nombresPersonas)
            case 4:
                print('Cerrando el programa')
                break
            case _:
                print('No es una opción válida')


