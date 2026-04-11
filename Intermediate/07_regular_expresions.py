import re

my_string = "Esta es la lección número 7: Expresiones regulares"
my_other_string = "Esta no es la lección número 7: Expresiones regulares"

print(re.match("Esta es la lección", my_string))
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones regulares", my_string))

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span() 
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forna de comprobar el None
# if match != None: # Otra forna de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print (my_other_string[start:end])