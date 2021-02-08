# mutavel: listas, dicionarios
# imutavel: tuplas, strings, numerom the true false, none

def lista_de_clientes(clientes_iteravel, lista_None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

lista_clientes_1 = ['Fabricio']
clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], lista_clientes_1)
clientes2 = lista_de_clientes(['Marcos', 'Jonas',  'Zico'])
cliente3 =lista_de_clientes(['José'])

print(clientes1)
print(clientes2)