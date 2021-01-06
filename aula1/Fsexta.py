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
younger_age = 20
older_age = 30


if age >= younger_age and age <= older_age:
    print(f'{name} can borrow')
else:
    print(f'{name} cant borrow')