"""
combinations, permutations e product 
combinação - ordem não importa
a,bos não repetem valores unicos
produto - Ordem importa e repete valores unicos
"""

from itertools import combinations, permutations, product, repeat

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for grupo in products(pessoas, repeat=2):
    print(grupo)