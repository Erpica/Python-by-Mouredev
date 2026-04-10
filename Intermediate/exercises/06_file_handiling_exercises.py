# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt", "w+")
my_phrase = "Hola desde Python"
text_file.write(my_phrase)
text_file.close()


# 2. Abre un archivo y lee todo su contenido.
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt")
print("\n2: ", text_file.readlines())
text_file.close()

# 3. Añade una nueva lí­nea al final del archivo con el texto "Lí­nea añadida".
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt", "a+", encoding="utf-8")
my_phrase_two = "\nLínea añadida"
text_file.write(my_phrase_two)
text_file.seek(0)
print("\n3: ", text_file.readlines())
text_file.close()

# 4. Lee solo los primeros 10 caracteres del archivo.
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt")
print("\n4: ", text_file.read(10))
text_file.close()

# 5. Usa seek para volver al inicio del archivo y leer desde ahí­.
# text_file.seek(0)

# 6. Lee e imprime el contenido lí­nea por lí­nea usando readline.
print("\n6: ")
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt")
text_file.seek(0)
number_of_lines = len(text_file.readlines())
text_file.seek(0)
for i in range(0, number_of_lines+1):
    print(text_file.readline(), end="")     

text_file.close()

# 7. Lee todas las lí­neas del archivo en una lista y recórrelas con un bucle.
print("\n7: ", end="") # Una forma maravillosa de que no de un salto de línea cuando ternia de escribir
text_file = open("Intermediate/exercises/file_handiling_exercises/text_file.txt")
text_file.seek(0)
for i in text_file.readlines():
    print(i, end="")

print("\n7: ", end="")
my_text = []

text_file.seek(0)
for i in text_file.readlines():
    print(i.strip())    # Otra forma de solucionar que no haga salto de línea
text_file.close()

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias lí­neas.
new_text_file = open("Intermediate/exercises/file_handiling_exercises/new_text_file.txt", "w+")
new_text_file.writelines("Hola.\n No se que hará esto.\n Pero, si no explota, algo habré aprendido.")

new_text_file.close()

# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.

text_to_write = "En el curso de Python\nVamos a hablar de lo mucho que nos gusta \nPython"
file_path = "Intermediate/exercises/file_handiling_exercises/new_text_file.txt"

def open_write_close(file_path, text_to_write):
    with open(file_path, "w+") as new_text_file:
        new_text_file.writelines(text_to_write)
    new_text_file.close()

open_write_close(file_path, text_to_write)

# 10. Lee un archivo lí­nea por lí­nea y muestra solo las que contienen la palabra "Python".
print("\n10: ", end="")
new_text_file = open("Intermediate/exercises/file_handiling_exercises/new_text_file.txt", "r+")
for line in new_text_file.readlines():
    if "Python" in line:
        print(line, end="")
new_text_file.close()

print("\n\nExtra: ", end="")
new_text_file = open("Intermediate/exercises/file_handiling_exercises/new_text_file.txt", "r+")
print(new_text_file.read())