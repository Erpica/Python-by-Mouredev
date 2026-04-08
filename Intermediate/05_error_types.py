### Error types ###

# SyntaxError
#print "¡Hola!"
print ("¡Hola!")

# NameError
#print (languaje)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Javascript"]
#print(my_list[4])
print(my_list[-1])

# ModuleNotFoundError
#import maths

# AttributeError
import math
#print(math.PI)

# KeyError
my_dict = {"Nombre": "Anto", "Apellido": "Pic", "Edad": 45}
#print(my_dict["Apelido"])

# TypeError
#print(my_list["Nombre"])

# ImportError
#from math import PI

# ValueError
my_int = int("10")
print(type(my_int))
my_int = "10"
print(type(my_int))
#my_int = int("10 años") # ValueError: invalid literal for int() with base 10: '10 años'

# ZeroDivisionError
#print (4/0)
