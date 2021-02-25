"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou o INIT')

    def __call__(self, *args, **kwargs):
        pass


a = A()
b = A()
c = A()

print(id(a), id(b), id(c))

##############################################################

print('----------------------------------------------------------------')


class A:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        self.__dict__[key] = value


a = A()
a.nome = 'Yasmim Vilen'
print(a.nome)
