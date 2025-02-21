elementos = ['marvel', 'rapidosfuriosos', 'bajoterra', 'mortalkombat', 'narnia']  # Lista inicial de elementos
def limpiar_lista(lista):
    """
    Función que elimina todos los elementos de una lista.
    :param lista: list - Lista que se desea limpiar.
    """
    lista.clear()  # Vacía la lista
# Muestra la lista antes de ser limpiada
print(f'La lista es: {elementos}')
# Llama a la función para limpiar la lista
limpiar_lista(elementos)
# Muestra la lista después de ser limpiada
print(f'La lista quedo asi: {elementos}')
