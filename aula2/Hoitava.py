# lists, tuplas, str -> Sequences -> Iterável
nome = 'Yasmim Vilen'
iterador = iter(nome)
gerador = (letra for letra in nome)
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('OLHA O FOR')

for letra in gerador:
    print(letra)

print('OLHA O OUTRO FOR')
for letra in gerador:
    print(letra)

print(next(gerador))
# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
    
# except:
#     pass

# print('CADÊ OS VALORES?')
# for valor in iterador:
#     print(valor)

# for letra in nome:
#     print(letra)
# print('#' * 80)

# for letra in nome:
#     print(letra)

# print(nome)

"""
atividade
"""
carrinho = []
carrinho.append(('produto 1', 30))
carrinho.append(('produto 2', '20'))
carrinho.append(('produto 3', 50))

total = sum([float(y) for x, y in carrinho])
print(total)