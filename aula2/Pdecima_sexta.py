from calculos import multiplica, PI

print(P1)
print(multiplica[1, 4])

"""
pacotes com python 
"""

from vendas.calc_preco import aumento,reducao
from vendas.formata import preco as preco2
preco = 49.90
preco_com_aumento = aumento(valor=preco, porcentagem=15, formata=True)
print(preco_com_aumento)

preco_com_reducao = reducao(valor=preco, porcentagem=15, formata=True)
print(preco_com_reducao)

print(preco2.real())

