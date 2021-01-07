print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
formatting values with modifiers
:s - texts (strings)
:d - integers (int)
:f - floating point numbers (float)
:.(NUMBERS)f - number of decimal places (float)
: (CARACTERE)(> or < or ^)(AMOUNT)(type - s, d or f

> - left
< - right
^ - center
"""
# example1
num_1 = 10
num_2 = 3
division = num_1 /num_2
print(f'{division:.2f}')

# example2
name = 'Yasmim Kalfeltz'
print(f'{name:s}')

# example3
num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10}')

# example4
name = 'Yasmim Kalfeltz'
print(len("##################"))
print(f'{name:#^50}')

# example5
name = 'Yasmim Kalfeltz'
formatted_name = '{n}'.format(n=name)
print(formatted_name)

# uppercase and lowercase
name = 'Yasmim Kalfeltz'
print(name.lower())  # letra minuscula
print(name.upper())  # letra maiuscula
print(name.title())  # primeiras letras maiusculas
