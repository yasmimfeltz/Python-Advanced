def s(saudacao, nome):
    print(f'{saudacao} {nome}')

s('Olá', 'Yamim')



def soma(n1, n2, n3):
        print(n1 + n2 + n3)

soma(2, 4, 8)
soma(1, 2, 3)
soma(1, 1, 1)

def aumento_percentual(valor, percentual):
    print(valor + (valor * percentual / 100))

aumento_percentual(50, 10)

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return'fizzbuzz, 3 e 5'
    if n % 5 ==0:
        return'buzz, 5'
    if n % 3 == 0:
        return'fizz, 3'
    return n

print(fb(7))
print(fb(10))
print(fb(15))
print(fb(22))

"""
Funções (def) - *args **kwargs - parte 3
"""
def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5,nome,a6)
    return nome, a6

var = func(1,2,3,4,5, nome='Yasmim')
print(var[0], var[1])

def func(*args):
    print(args)

lista = [1,2,3,4,5]
n1, n2, *n = lista
print(n1, n2, n)

def func(*args, **kwargs):
    args = list(args)

    idade = kwargs['idade']
    print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Yasmim', sobrenome='Kalfeltz')

"""
parte 4
"""
variavel = 'valor'

def func():
    outra_variavel = 'valor'
    return outra_variavel
def func2(arg):
    print(arg)

var = func()
func2(var)

"""
Exercício
"""
def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

print(ola_mundo())

"""
exercicio 2
"""
def mestre(funcao, *args, **kwargs):
    return  funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}'

def saudacao(nome,saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Yasmim')
executando2 = mestre(saudacao, 'Yasmim', saudacao= 'Bom dia!')
print(executando)
print(executando2)