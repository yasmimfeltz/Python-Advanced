"""
Geradores, Iteradores e iteráveis em python
"""

lista = [0,1,2,3,4,5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '_next_'))

# exemplo 2
import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()

for v in g:
    print(v)

# exemplo3
import sys
import time

def gera():
    variavel = 'valor 1'
    yield  variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel

g = gera()

for v in g:
    print(v)

# exemplo 4

import sys
import time

l1 = [x for x in range(1000000)]
l2 = (x for x in range(1000000))

for v in l2:
    print(v)