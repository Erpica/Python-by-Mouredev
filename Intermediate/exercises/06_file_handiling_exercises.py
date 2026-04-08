# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt", "w+")
my_phrase = "Hola desde Python"
text_file.write(my_phrase)
text_file.close()


# 2. Abre un archivo y lee todo su contenido.
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt")
print(text_file.readlines())
text_file.close()

# 3. Añade una nueva lí­nea al final del archivo con el texto "Lí­nea añadida".
text_file = open ("Intermediate/exercises/file_handiling_exercises/text_file.txt", "w+")
my_phrase_two = "\nLí­nea añadida"
text_file.write(my_phrase_two)
print(text_file.readlines())

# 4. Lee solo los primeros 10 caracteres del archivo.

# 5. Usa seek para volver al inicio del archivo y leer desde ahí­.

# 6. Lee e imprime el contenido lí­nea por lí­nea usando readline.

# 7. Lee todas las lí­neas del archivo en una lista y recórrelas con un bucle.

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias lí­neas.

# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.

# 10. Lee un archivo lí­nea por lí­nea y muestra solo las que contienen la palabra "Python".