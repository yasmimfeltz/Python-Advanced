from dados import produtos, pessoas, lista
from functools import reduce

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p


nomes = map( aumenta_idade, pessoas)

for pessoa in nomes:
    print(pessoa)

"""
FILTER
"""

def filtra(pessoa):
    if pessoa['idade'] >=18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)

for produto in nova_lista:
    print(produto)


"""
REDUCE
"""

soma_idades = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(soma_idades / len(pessoas))