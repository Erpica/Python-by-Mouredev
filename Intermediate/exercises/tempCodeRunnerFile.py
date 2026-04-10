
# 10. Lee un archivo lí­nea por lí­nea y muestra solo las que contienen la palabra "Python".
new_text_file = open("Intermediate/exercises/file_handiling_exercises/new_text_file.txt", "r+")
for line in new_text_file.readlines():
    if "Python" in line:
        print(line, end="")