from itertools import groupby

alunos = [
    {'nome': 'Yasmim', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'C'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)


for agrupamento, valores_Agrupados in alunos_agrupados:
    var1, var2 = tee(valores_Agrupados)

    print(f'Agrupamento:{agrupamento}')

    for aluno in var1:
        print(aluno)

    quantidade = len(list(var2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()