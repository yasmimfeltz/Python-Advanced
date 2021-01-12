print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
python lists
Slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""
#        0    1    2    3    4    5
list = ['A', 'B', 'C', 'D', 'E', 10.5]
list[5] = 'something.'

print(list[5])
print(list[0:3])
print(list[:3])
print(list[::2])
print(list[::-1])

# example 2
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.append('b')
l1.extend(l2)
l2.insert(0, 'monkey')
l3 = l1 + l2

print(l2[0])
print(l1)

# example 3
l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

# example 4
#     0 1 2 3 4 5 6 7 8
l2 = [1,2,3,4,5,6,7,8,9]
print(max(l2))
print(min(l2))

for v in l2:
    print(v)

soma = 0
for valor in l2:
    soma = soma + valor
print(soma)

# example 5
l5 = ['String', True, 10, -20.5]

for elem in  l5:
    print(f'o tipo de elem é {type(elem)} e o seu valor é {elem}')

# example 6
secret = 'perfume'
digitadas = []

while True:
    letter = input('enter a letter: ')

    if len(letter) > 1:
        print('ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letter)

    if letter in secret:
        print(f'uhuul, a letra "{letter}" existe na palavra secreta')
    else:
        print(f'aff, a letra "{letter}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secret:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secret:
        print(f'você ganhou!!. a palavra era {secreto_temporario}')
        break
    else:
        print(f'a palavra secreta está assim {secreto_temporario}')