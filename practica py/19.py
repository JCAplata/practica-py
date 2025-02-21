frase = input('Escribe una frase: ')  # Solicita al usuario que ingrese una frase
listaPalabras = frase.split()  # Divide la frase en palabras individuales y las almacena en una lista
print(listaPalabras)  # Muestra la lista de palabras obtenida
palabrasUnidas = ' '.join(listaPalabras)  # Une nuevamente las palabras con espacios entre ellas
print(palabrasUnidas)  # Imprime la frase reconstruida
