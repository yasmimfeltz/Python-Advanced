from random import randint
numero = str(randint(100000000, 999999999))

new_cpf = numero
reverso = 10  # Contador reverso
total = 0
# Loop de cpf
for index in range(19):
    if index > 8:
        index -= 9

    total += int(new_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        new_cpf += str(d)

    print(new_cpf)