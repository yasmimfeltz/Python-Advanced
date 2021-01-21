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
