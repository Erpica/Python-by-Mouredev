### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_add_value(5,2, sum_one))
print(sum_two_values_and_add_value(5,2, sum_five))

### Closures ###
# Es una función que retorna una función

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_clousure = sum_ten(1)
print (add_clousure(5))
print (sum_ten(1)(5))

### Buit-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map: 
# Siempre va a necesitar un conjunto iterable, como una lista de valores.
# Al ser una función de orden superior puede ejecutar otras funciones
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number*2, numbers)))

# Filter: 

def filter_greater_thet_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_thet_ten, numbers)))
print(list(filter(lambda number:number>10, numbers)))

# Reduce:
# Le paso función y lista. Coge los dos primeros hace lo que dice la función y le va haciendo lo mismo al resto. Al final un número
def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

print(reduce(sum_two_values, numbers))
print(reduce(lambda num1, num2: num1 + num2, numbers))