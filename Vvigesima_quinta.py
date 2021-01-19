print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
operador ternario 
"""
logged_user = True

if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'

print(msg)

# example 2
idade = 18
if idade >= 18:
    print("pode acessar.")
else:
    print('não pode acessar.')

# versão simplificada
idade = 18
e_de_maior = (idade>= 18)
msg = 'pode acessar' if e_de_maior else 'não pode acessar.'
print(msg)