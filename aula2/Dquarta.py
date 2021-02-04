print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
"""
dicionários em python 
"""
d1 = {'Chave1': "Valor da chave"}
print(d1)

d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1['nova_chave'] = 'Valor da nova chave'

print(d1)

# chaves ou tem que ser todas iguais, ou todas diferentes. Diferentes se quiser valores diferentes.

d2 = {1: 'valor1', 2: 'valor2', 3: 'valor3'}
d3 = {'chave': 'valor', 'chave': 'valor', 'chave': 'valor'}
print(d3)
print(d2)

d1 = {
    'str': 'valor',
    123: 'outro valor',
    (1,2,3,4): 'tupla',
}

d1['naoexiste'] = 'Agora existe.'
if 'naoexiste' in d1:
    print(d1['naoexiste'])

print('oi')

d5 = {
    'str' : 'valor',
    123: 'Outro valor',
    (1,2,3,4) : 'Tupla',
}

d5.update({'nova_chave' : 'novo_valor'})

if d1.get('str') is not None:
    print(d1.get('nova_chave'))

print(123)

d8 = {
    1: 2,
    2: 3,
    4: 5,
}

d9 = {
   'a' : 'b',
    'c' :'d',
}
d8.update(d9)
print(d8)

"""
sistema de perguntas e respostas
"""

print()
print('Texto explicativo.')

perguntas = {
    'pergunta1': {
        'pergunta': 'quanto é 2+2:',
        "respostas": {'a': '1','b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': 'a','b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
}
print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')


    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input(('Sua resposta: '))
    if resposta_usuario == pv['resposta_certa']:
        print("EHHHHHH!!! você acertou!!!")
        respostas_certas += 1
    else:
        print("IXXIIII!!! você errou!!!")

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'sua porcentagem de acerto foi de {porcentagem_acerto}%.')