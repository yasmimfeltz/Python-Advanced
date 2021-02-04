"""
list comprehension em compreensão de dicionarios
"""

l1 = [1,2,3,4,5,6,7,8,9]
ex = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Yasmim', 'Vilen', 'Kalfeltz']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y,x) for x,y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 ++ 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 else 0 for v in l3]
print(ex7)

"""
exercicios
"""
string = '12345678901234567890123456789012345678901234567890'
n = 10
contadores = [i for i in range(0, len(string), n)]
tuplas = [(i, i + n) for i in range(0, len(string), n)]
lista = [string[i:i + n] for i in range(0, len(string), n)]
raw = [f'string[{i}:{i + n}]' for i in range(0, len(string), n)]
retorno = '.'.join(lista)
print(contadores)
print(tuplas)
print(raw)
print(lista)
print(retorno)

"""
dicionario comprehension
"""
l1 = [1,2,3,4,5,6]
l2 = [v*2 for v in l1]
print(l2)

# exemplo 2
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {x: y for x,y in lista}
print(d1)

# exemplo 3

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1, type(d1))