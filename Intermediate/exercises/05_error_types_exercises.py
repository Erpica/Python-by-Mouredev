#1. Genera un SyntaxError al imprimir una cadena sin paréntesis.
print("* SyntaxError:\n  print \"hola\"")

#2. Genera un NameError intentando usar una variable no definida.
print("\n* NameError:\n  b = a + c")

#3. Genera un IndexError accediendo a un índice inexistente de una lista.
my_list = [1, 2, 3]
print("\nmy_list = [1, 2, 3]")
print("* IndexError:\n  print (my_list[3])")

# 4. Genera un ModuleNotFoundError al importar un módulo inexistente.
print("\n* ModuleNotFoundError:\n  import maths")

# 5. Genera un AttributeError accediendo a un atributo que no existe.
import math
print("\nimport math")
print("* AttributeError:\n  print (math.PI)")

# 6. Genera un KeyError al acceder a una clave inexistente de un diccionario.
my_diccionary = {
    "Nombre": "Anto",
    "Apellido": "Pic"
}
print("\nmy_diccionary = {\"Nombre\": \"Anto\", \"Apellido\": \"Pic\"}")
print ("* KeyError: \n  my_diccionary[\"Apellidos\"]")

# 7. Genera un TypeError usando tipos incorrectos (índice string en lista).
print ("\n* TypeError: \n  my_list[\"Apellido\"]")

# 8. Genera un ImportError al importar una función que no existe desde un módulo.
print("\n* ImportError:\n  from math import PI")

# 9. Genera un ValueError intentando convertir un string no numérico a entero.
my_string = "10 o más"
print("\nmy_string = \"10 o más\"")
print("* ValueError:\n  my_number = int(my_string)")

# 10. Intenta detectar si un error ocurre usando try-except con un KeyError.
try:
    print (my_diccionary["Apellidos"])
except KeyError:
    print("Revisa la key porque está mal escrita")