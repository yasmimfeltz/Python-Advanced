print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
Relational operations: == > >= < <= != and IF, ELIF, ELSE 
== equals
> plus 
>= plus or equals
< minus
<= minus or equals
!= different
"""
# examples

var_1 = 'Yasmim' #str
var_2 = 'Kalfeltz' #str

expression = (var_1 != var_2)
print(expression)

#example2
name = input("enter your name:")
age = input("enter your age:")
age = int(age)
#age limit for borrowing
age_limit = 18

if age >= age_limit:
    print(f'{name} can borrow')
else:
    print(f'{name} cant borrow')