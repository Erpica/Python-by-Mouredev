### Challenges ###

"""
EL FAMOSO "FIZZ BUZZ":
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de lÃ­nea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""



#[print(element) for element in ["fizzbuzz" if (i % 3 == 0 and i % 5 == 0) else "fizz" if (i % 3 == 0 ) else i for i in range(1, 101)]]

'''
# Y por Brais
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()
'''

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

string1= "amor"
string2= "Roma"

def is_anagram(string1, string2):
    #anagrama = False
    count = 0
    if (len(string1) == len(string2) and string1.lower() != string2.lower()):
        for element1 in string1:
            for element2 in string2:
                if (element1.lower() == element2.lower()):
                    count += 1
    if(count == len(string1)):
        return True
    return False
    
print (is_anagram(string1, string2))
                
'''
# Y por Brais
def is_anagram2(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram2("Amor", "Roma"))
'''

"""
LA SUCESIóN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci ():
    fibonacci_list = [0, 1]
    for i in range(1, 49):
        fibonacci_list.append(fibonacci_list[i-1]+fibonacci_list[i])
    return fibonacci_list
        
print (len(fibonacci()))
'''
# Y por Brais
def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()
'''


"""
¿QUÉ ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""


for i in range (3, 101):
    divisible = False
    for j in range (2, i):
        if i % j == 0:
            divisible = True
    if divisible == False:
            print(i)


'''
# Y por Brais
def is_prime():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)

is_prime()
'''            

'''
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornará "odnum aloH"
'''
my_string = "Cadena de ejemplo"


def reverse_string(my_string):
    reversing = []
    for i in range(len(my_string)):
        number = len(my_string)-i
        reversing.append(my_string[number-1])
    return "".join(reversing)
print (reverse_string(my_string))
    
'''
y por Brais:

def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for index in range(0, text_len):
        reversed_text += text[text_len - index - 1]
    return reversed_text


print(reverse("Hola mundo"))
'''






















