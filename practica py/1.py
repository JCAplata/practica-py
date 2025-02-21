import os
# Lista para almacenar las frutas ingresadas por el usuario
frutas = []
print('Escribe tres frutas')
def ListaFrutas():
    """
    Función que retorna un mensaje con la lista de frutas ingresadas.
    :return: str - Mensaje con las frutas ingresadas.
    """
    return f'tus frutas son: {frutas}'
# Bucle infinito para solicitar la entrada de frutas
while True:
    fruta1 = input('di una fruta: ')  # Solicita la primera fruta
    if fruta1.isalpha():  # Verifica si la entrada solo contiene letras
        frutas.append(fruta1)  # Agrega la fruta a la lista
        fruta2 = input('di otra fruyta: ')  # Solicita la segunda fruta
        if fruta2.isalpha():  # Verifica si la entrada solo contiene letras
            frutas.append(fruta2)  # Agrega la fruta a la lista
            fruta3 = input('la ultima fruta: ')  # Solicita la tercera fruta
            if fruta3.isalpha():  # Verifica si la entrada solo contiene letras
                frutas.append(fruta3)  # Agrega la fruta a la lista
                listaFrutas = ListaFrutas()  # Llama a la función para obtener el mensaje
                print(listaFrutas)  # Imprime el mensaje con las frutas ingresadas
                break  # Sale del bucle
            else:
                print('La fruta no lleva caracteres especiales')  # Mensaje de error si hay caracteres no alfabéticos
        else:
            print('La fruta no lleva caracteres especiales')  # Mensaje de error si hay caracteres no alfabéticos
    else:
        print('La fruta no lleva caracteres especiales')  # Mensaje de error si hay caracteres no alfabéticos

        
