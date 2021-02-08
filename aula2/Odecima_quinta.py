def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1 / n2

try:
    print(divide(n1=2,n2=0))
except ValueError as error:
    print('Você está tentando dividir por 0')
    print('log:', error)


"""
uso de try e except no condicional
"""
def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass

while True:
    numero = converte_numero(input('digite um numero: '))
    if numero is None:
        print("Erro, isso não é um numero")
    else:
        print(numero * 2)