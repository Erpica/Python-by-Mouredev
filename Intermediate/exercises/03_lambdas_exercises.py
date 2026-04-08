# 1. Crea una lambda que sume dos números.
my_sum_lambda = lambda num1, num2: (num1 + num2)
print(my_sum_lambda(2,3))

# 2. Crea una lambda que calcule el cuadrado de un número.
my_square_lambda = lambda num3: num3**2
print(my_square_lambda(3))

# 3. Crea una lambda que devuelva el mayor de dos números.
# Recuerda: A if B else C
my_bigger_lambda = lambda num4, num5: num4 if (num4>num5) else num5
print(my_bigger_lambda(7, 4))

# 4. Crea una lambda que sume 10 a un número dado.
my_sum10_lambda = lambda n: n+10
print(my_sum10_lambda(20))

# 5. Crea una lambda que devuelva el último carácter de una cadena.
my_return_last_lambda = lambda string: string[len(string)-1]
print(my_return_last_lambda("Hola que tal"))

# 6. Crea una lambda que indique si una palabra tiene más de 6 letras.
my_sixletters_lambda = lambda string2: "No tiene tantas o son más de una palabra" if (len(string2)<6 or string2.find(" ")>0) else "Tiene más de seis letras."
print(my_sixletters_lambda("hola que tal"))

# 7. Crea una lambda que convierta una cadena a minúsculas.
my_minusc_word = lambda string3: string3.lower()
print(my_minusc_word("HolA"))

# 8. Crea una lambda que devuelva True si un número es positivo.
my_positive_num = lambda num6: True if num6 > 0 else False
print(my_positive_num(-4))

# 9. Crea una lambda que devuelva "Cadena vací­a" si el string está vacío.
empty_string = lambda string4: "Cadena vacía" if (len(string4) == 0) else "Algo hay"
print(empty_string("33"))

# 10. Crea una lambda que calcule el precio final con un impuesto añadido del 21%.
my_tax = lambda num7: num7*1.21
print(my_tax(10))


print(sum_three_values(5)(2,4))
