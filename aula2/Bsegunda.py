print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
"""
Expressões lambda ( funções anônimas )
"""
a = lambda x, y: x * y

print(a(2, 2))

# Exemplo de como utilizar ela

lista = [
    ['p1', 13],
    ['p2', 6],
    ['p3', 7],
    ['p4', 50],
    ['p5', 8],
]
lista.sort(key=lambda item: item[1], reverse=True)  # modo de alterar a ordem da lista
print(sorted(lista,key=lambda i: i[0], reverse=True))
print(lista)