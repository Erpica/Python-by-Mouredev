import re

my_string = "Esta es la lección número 7.\nLección llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 7: Expresiones regulares"

print(re.match("Esta es la lección", my_string))
print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones regulares", my_string))

match = re.match("Esta es la lección", my_string, re.I) # re.I -> IgnoreCase
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

# search # Solo encuentra la primera ocurrencia
search = re.search("lección", my_string, re.I)
start, end = search.span() 
print(my_string[start:end])

# findall # Encuentra todas las veces que aparece 
findall = re.findall("lección", my_string, re.I)
print(findall)

# split
print(re.split("\n", my_string))

# sub
print(re.sub("Expresiones regulares", "RegEx", my_string)) # Aquí esto no hace nada: re.I
print(re.sub("Lección|lección", "LECCIÓN", my_string))
print(re.sub("[L|l]ección|lección", "LECCIÓN", my_string))