print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
logical operators
and, or, not
in e not in
"""
# in "And" the two have to be true to return true
# the "OR" needs one of the two to be true
# the "not" just needs an expression

a = 2
b = 3

name = "Yasmim"

if 'a' in name:
    print('exist')
else:
    print('doesnt exist')

user = input('user name:')
password = input('user password:')

user_bd = 'yasmim'
password_bd = "12345"

if user_bd == user and password_bd == password:
    print('you are logged in the system')
else:
    print('you are not logged into the system')

