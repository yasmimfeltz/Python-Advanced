"""
Polimorfismo é o principio que permite que aula_class derivadas de uma mesma superclasse tenham
métodos iguais (da mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro assunto')