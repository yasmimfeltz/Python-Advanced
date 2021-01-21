print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
"""
Funções - def em Python (Parte 1)
"""


def funcao():
    print('so linda')


funcao()
funcao()
funcao()


def funcao(gat):  # tem como renomear essa função e em todas as vezes que ela foi chamada usando refactor
    print(gat)

funcao('gathusca')


def funcao(alo, marciano):
    print(alo, marciano)

funcao('Yasmim', 'Kalfeltz')
funcao('15', 'anos')

def saudacao(msg= 'eai', nome='bro'):
    nome = nome.replace('r', '3')
    msg = msg.replace('i', '4')
    return f'{msg} {nome}'

var = saudacao()
print(var)


def funcao2(var):
    return(var)

variavel = funcao2('Valor que eu quero')

def divisao(n1,n2):
    if n2 == 0:
        return

    return n1 / n2

divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('conta inválida')

def dumb():
    return [1,2,3,4,5]

print(dumb(), type(dumb()))

def dumb():
    return ('Luiz', 'Otávio')

var = dumb()

print(var[1], type(var))