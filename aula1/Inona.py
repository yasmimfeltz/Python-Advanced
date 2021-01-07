print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
Built-in documentation and functions Useful
"""
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
# functions: isnumeric isdigit isdecimal
# isnumeric returns numbers and positive {12345}
print(num1.isnumeric())
print(num2.isnumeric())

# ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
"""
links = https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py
and = https://docs.python.org/3/library/stdtypes.html#strisdecimal
"""
# to solve the problem now
num1 = input('Enter a number: ')
num2 = input('Enter another number: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')
