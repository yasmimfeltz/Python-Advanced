print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
Split, Join, Enumerate em python
* Split - dividir em uma string #str
* Join - Juntar uma lista #str
Enumerate - Enumerar elementos da lista #list / iteráveis
"""
string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_2:
    print(valor.strip().capitalize())  # .captalize deixa a primeira letra maiuscula

# example 2 função join

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ','.join(lista)

print(string2)

# example 3
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

# example 4
lista = ['Yasmim','Giovana','Isabel']

for indice, nome in enumerate(lista):
    print(indice, nome)