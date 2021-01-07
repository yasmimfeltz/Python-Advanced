# print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
# """
# while in python
# used to perform actions while a condition is true
# """
# # while True: #loop será executada até que seja falsa, como já esta determinado true, ele nunca sera falso
# #     name = input("what is your name: ")
# #     print(f'hello {name}!')
#
# # example
# while True:
#     print()
#     num_1 = input("Enter a number: ")
#     num_2 = input("Enter another number")
#     operator = input("enter a operator")
#     leave = input('do you want to leave?: [y]es or [n]o')
#
#     if leave == 'y':
#         break
#
#     if not num_1.isnumeric() or not num_2.isnumeric():
#         print("you need to enter a number or leave")
#         continue
#
#     num_1 = int(num_1)
#     num_2 = int(num_2)
#
#     # + - / *
#     if operator == "+":
#         print(num_1 + num_2)
#     elif operator == "-":
#         print(num_1 - num_2)
#     elif operator == '/':
#         print(num_1 / num_2)
#     elif operator == '*':
#         print(num_1 * num_2)
#     else:
#         print('Operador inválido')

"""
WHILE AND ELSE
accountants
accumulators
"""

counter = 1
accumulator = 1

while counter <= 10:
    print(counter, accumulator)

    accumulator = accumulator + counter
    counter += 1
else:
    print("bye")
