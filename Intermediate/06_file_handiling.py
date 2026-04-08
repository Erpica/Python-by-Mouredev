### File Handling ###

# .txt file
import os

# txt_file = open("Intermediate/my_file.txt") # Abre el archivo en modo lectura (read mode)
txt_file = open("Intermediate/my_file.txt", "w+")
txt_file.write("Mi nombre es Anto\nMi apellido es Pic\nTengo 45 años\nY mi lenguaje favorito es Python")
# print(txt_file.read()) # => lo lee entero y deja el cursor al final
# print(txt_file.read(10)) # => Lee los primeros 10 caracteres del archivo (o donde esté el "cursor")
# print(txt_file.readline()+txt_file.readline())
# print(txt_file.readline())
# print(txt_file.readlines())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque trabajo más con Javascript")

for line in txt_file.readlines():
    print(line)

txt_file.close()
#os.remove("Intermediate/my_file.txt")

# .json file
import json
json_file = open("Intermediate/my_file.json", "w+")
json_test = {
    "name": "Anto",
    "surname": "Pic", 
    "age": 45,
    "languaje": [
        "Python",
        "Javascript",
        "PHP"
    ],
    "website": "erpica.es"
}

# dump: para escribir en un fichero json
json.dump(json_test, json_file, indent = 2) # indent para la estética del json
# json.dump(json_test, json_file, indent = 2) # Si lo pongo otra vez me dará error porque escribe directamente donde se ha quedado el cursor

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)


json_dict = json.load(open("Intermediate/my_file.json"))
print(type(json_dict))


# .csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languaje", "website"])
csv_writer.writerow(["Anto", "Pic", 45, "Python", "erpica.es"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)