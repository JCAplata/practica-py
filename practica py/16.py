tareas = []  # Lista para almacenar las tareas
while True:
    try:
        # Solicita al usuario seleccionar una opción del menú
        menu = int(input('Menu:\n 1. Agregar tarea\n 2. Mostrar tareas\n 3. Eliminar tarea\n 4. Salir\nIngrese seleccion: '))
    except(ValueError):
        print('Ingrese una opción válida (1, 2, 3 o 4)')
    else:
        match menu:
            case 1:
                # Agregar una nueva tarea a la lista
                tarea = input('Ingrese tarea: ')
                tareas.append(tarea.capitalize())
            case 2:
                # Mostrar todas las tareas registradas
                print(f'Estas son las tareas: {tareas}')
            case 3:
                # Eliminar una tarea si existe en la lista
                tareaR = input('Ingrese tarea que desea remover: ')
                if tareaR.capitalize() in tareas:
                    tareas.remove(tareaR.capitalize())
                else:
                    print('La tarea no está en la lista')
            case 4:
                # Salir del menú
                print('Cerrando menú...')
                break
            case _:
                print('Ingrese una opción válida')
