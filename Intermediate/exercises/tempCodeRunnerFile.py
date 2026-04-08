text_file = open ("Intermediate/exercises/file_handiling_exercises/text_file.txt", "w+")
my_phrase_two = "Lí­nea añadida"
text_file.write(my_phrase_two)
print(text_file.readlines())