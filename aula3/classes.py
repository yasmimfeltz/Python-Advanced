class CarrinhoDeCompras:
    def __init__(self):
        self.produto = []

    def inserir_produto(self,produto):
        self.produto.append(produto)

    def lista_produto(self):
        for produto in self.produto:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produto:
            total += produto.valor
        return total

    class Produto:
        def __init__(self, nome, valor):
            self.nome = nome
            self.valor = valor


#############################################################################################
# new

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade,estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')

#################################################################
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')

    class Cliente(Pessoa):
        def comprar(self):
            print(f'{Self.nomeclasse} comprando...')

    class Aluno(Pessoa):
        def estudar(self):
            print(f'{self.nomeclasses} estudando...')