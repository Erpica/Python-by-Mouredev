print("1. Genera una lista utilizando comprensión con los números del 0 al 10.")
my_list = [i for i in range(11)]
print(my_list)

print("\n2. Crea una lista utilizando comprensión con los cuadrados de los números del 1 al 10.")
my_square_list = [i**2 for i in range(1, 11)] # o pow(i,2)
print (my_square_list)


print("\n3. Genera una lista utilizando comprensión con los números pares del 0 al 20.")
#even_list = [i for i in range(0, 21, 2) ]
even_list = [i for i in range(0, 21) if i % 2 == 0]
print(even_list)

print("\n4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensión.")
my_celsius_list = [10, 30, 24, 7, 31]
print ([(element * 9/5) +32 for element in my_celsius_list])

print("\n5. Crea una lista utilizando comprensión con los caracteres de una cadena.")
my_string = "Esta sería mi cadena, por ejemplo."
my_string_list = [caracter for caracter in my_string]
print(my_string_list)

print("6. Filtra una lista de palabras y deja solo las que tienen más de 4 letras utilizando comprensión.")
my_words_list = ["hola", "adios", "buenas", "aaai"]
my_filtered_words_list = [element for element in my_words_list if len(element) == 4]
print(my_filtered_words_list)

print("\n7. Aumenta en 5 cada número de una lista con comprensión usando una función externa.")
def number_plus_5 (number):
    return number + 5

my_plus_5_list = [print(number_plus_5(element)) for element in my_celsius_list]

print("\n8. Crea una lista de booleanos que indique si cada número es mayor que 10 utilizando comprensión.")
my_boolean_list = [True if (element > 10) else False for element in my_celsius_list]
print (my_boolean_list)

print("\n9. Multiplica solo los números impares por 3 en una lista utilizando comprensión.")
my_new_list = [element*3 for element in my_celsius_list if element % 2 != 0]
print (my_new_list)

print("\n10. Usa comprensión de listas anidada para generar una matriz 3x3 con números del 1 al 9.")
my_list_one =[1, 2, 3]
my_list_two =[4, 5, 6]
my_list_three =[7, 8, 9]

matrix = [[(i * 3 + j + 1) for j in range(3)] for i in range(3)]
for fila in matrix:
    print(fila)