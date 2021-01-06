print("Hello World")
# comments

"""
another type of comments
"""

print('Yasmim', 'Kalfeltz', sep='-', end='━━━━━━✦✗✦━━━━━━━')
print('15', 'yrs', sep='-', end=' ')

"""
str - string
"""

print("something")  # texts within quotation marks
print("this is my \"text\" ")  # way to use "" as text within a string

# \n line break.. example
print('her husband is so toxic \n but who am i to judge')

"""
Data types
str - string = texts like 'this' or "this"
int - integer = 79 - 0 - 8293 - 10000 - 10
float - floating point real values = 34.34 - 1.5 - 10.5 
bool - boolean = true or false
"""
print('Yasmim', type('Yasmim'))  # str
print(10, type(10))  # int
print('25.23', type('25.23'))  # float
print('l' == 'l', type('l' == 'l'))  # bool

# string: name
print('Yasmim', type('Yasmim'))
# int: age
print(15, type(15))
# float = height
print(1.60, type(1.60))
# is of age
print(15 < 18, type(15 < 18))

"""
+, -, *, /, //, **, %, ()
"""

print(20 * 'A')
print(20 * 2)
print('20' + 'A')
print(20 + 2)

"""
start with letter, can contain numbers, separate _, lowercase letters
"""
name = 'Yasmim'
age = 15
height = 1.60
weight = 62
it_is_bigger = age > 18
date_1 = True
current_date = 2019
imc = weight / height ** 2

print(name, 'is', age, 'years old and her IMC is:',imc)
