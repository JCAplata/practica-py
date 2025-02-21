contactos = []  # Lista para almacenar los contactos
def agregarContacto(lista):
    """Función para agregar un contacto a la lista."""
    nombre = input('Escribe el nombre del contacto: ')
    telefono = input('Escribe el numero de telefono (10 digitos): ')
    if len(telefono) == 10:  # Verifica que el número tenga exactamente 10 dígitos
        contacto = {'Nombre': nombre, 'Telefono': telefono}  # Crea un diccionario con los datos del contacto
        lista.append(contacto)  # Agrega el contacto a la lista
        print(f'Los contactos son: {lista}')  # Muestra la lista actualizada
    else:
        print('Un teléfono tiene 10 dígitos')  # Mensaje de error si el número no tiene 10 dígitos
agregarContacto(contactos)  # Llama a la función para agregar un contacto
