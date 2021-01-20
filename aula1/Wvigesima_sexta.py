print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
nome = input("digite o seu nome: ")
if nome:
    print('olá', nome)
else:
    print('Você não digitou nada:c ')

# modo mais facil
nome = input("digite o seu nome: ")
print('olá',nome or "você não digitou nada :c")

# proximo exemplo
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Luiz'

variavel = a or b or c or d or e or f or g

print(variavel)
