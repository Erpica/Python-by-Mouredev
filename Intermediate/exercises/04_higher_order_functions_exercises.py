# 1. Crea una función que reciba una función y un número, y devuelva el resultado de aplicar la función al número.
from functools import reduce


def square_function(num):
    return num ** 2

def my_function_f_n(f,n):
    return square_function(n)

print(my_function_f_n(square_function, 5))

# 2. Crea una función que reciba dos números y una función, y devuelva el resultado de sumar los dos números y aplicar la función.
def my_function_2n_f(num1, num2, f):
    return f(num1+num2)

print(my_function_2n_f(4, 3, square_function))

# 3. Crea una función que devuelva otra función que sume un número fijo.
def sum_function(num):
    return num + 2

def my_function_f(num):
    return sum_function(num)

print(my_function_f(12))

# 4. Usa map() con lambda para multiplicar cada número de una lista por 10.
my_list = [2, 4, 6, 7]

print(list(map(lambda num: num * 10, my_list)))

# 5. Usa filter() con lambda para quedarte solo con los números pares.
print (list(filter(lambda num: num % 2 == 0, my_list)))

# 6. Usa reduce() con lambda para obtener la suma total de una lista.
print(reduce(lambda num1, num2: num1 + num2, my_list))

# 7. Escribe una función que devuelva una función que reciba un nombre y devuelva "Hola, nombre".
def greet_fabric ():
    def greet(name):
        return f"hola, {name}"
    return greet

my_greet = greet_fabric()
print(my_greet("Anto"))

# 8. Crea una función que reciba una lista y una función, y cuente cuántos elementos cumplen con la función.
def check_function(my_list, condition):
    count = 0
    for element in my_list:
        if condition(element):
            count += 1
    return count

print(check_function([1, 5, 8, 3], lambda x: x > 4))

# 9. Crea una función que reciba dos funciones y un número, y las aplique en orden.
def apply_both(f1, f2, value):
    return f2(f1(value))

print(apply_both(lambda x: x + 2, lambda x: x * 3, 4))

# 10. Crea una función que reciba una lista y una función, y aplique esa función a cada elemento usando un bucle (sin map).
def apply_to_list(lst, f):
    result = []
    for item in lst:
        result.append(f(item))
    return result