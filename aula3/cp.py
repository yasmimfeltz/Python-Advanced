from classes.conta import Conta

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insifuciente')
            return

        self.saldo -= valor
        self.detalhes()