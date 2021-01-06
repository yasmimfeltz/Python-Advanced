print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
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

print(name, 'is', age, 'years old and her IMC is', imc)
print(f'{name} is {age} years old and her IMC is {imc: .2f}')
print('{} is {} years old and her IMC is {:.2f}'.format(name, age, imc))

# way of calling the variable and changing places several times
print('{0} is {1} years old and her IMC is {2:.2f}'.format(name, age, imc))
# ▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
print('{2:.2f} {1} {0} is {1} years old and her IMC is {2:.2f}'.format(name, age, imc))

# ◢◤◢◤◢◤◢◤◢◤◢◤◢◤Atividade◢◤◢◤◢◤◢◤◢◤◢◤◢◤
print('◢◤◢◤◢◤◢◤◢◤◢◤◢◤ Atividade ◥◣◥◣◥◣◥◣◥◣◥◣◥◣')

name = 'Yasmim'
age = 15
height = 1.60
weight = 62
year = 2020
imc = weight / height
birth = age - year

print(f'{name} is {age} years old and {height} tall')
print(f'{name} weighs {weight} and her imc is {imc:.2f} tall')
print(f'{name} was born in {birth}\n \n ')
