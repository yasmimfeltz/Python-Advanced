print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
print('◢◤◢◤◢◤◢◤◢◤◢◤◢◤ Atividade ◥◣◥◣◥◣◥◣◥◣◥◣◥◣')
numberint = input('insert an number integer: ')

if not numberint.isdigit():
    print('This is not an integer')
else:
    numberint = int(numberint)


    if not numberint % 2 == 0:
        print(f"{numberint} odd")
    else:
        print(f"{numberint} even")

print('◢◤◢◤◢◤◢◤◢◤◢◤◢◤ Atividade2 ◥◣◥◣◥◣◥◣◥◣◥◣◥◣')
horary = input('Enter an Horary (0-23): ')

if horary.isdigit():
    horary = int(horary)

    if horary < 0 or horary > 23:
        print("the time must be between 0 and 23")
    else:
        if horary < 11:
            print("Good Morning")
        elif horary <= 17:
            print('Good Afternoon')
        else:
            print('Good Night')
else:
        print('please enter a time between 0 and 23')

print('◢◤◢◤◢◤◢◤◢◤◢◤◢◤ Atividade3 ◥◣◥◣◥◣◥◣◥◣◥◣◥◣')
name = input('Enter your name: ')
size = len(name)  # tamanho

if size <= 4:
    print('Your name is short')
elif size <= 6:
    print('your name is normal')
else:
    print('your name is too big')