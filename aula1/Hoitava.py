print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
LEN function returns the number of items in an object. When the object is a string
"""
user = input("Enter your user: ")
number_of_characters = len(user)

if number_of_characters < 6:
    print('you need at least 6 characters')
else:
    print('you were registered in the system')

# example2
string1 = input('anything')
string2 = input('anything2')

# int shows error with int and float
print(len(string2))  # the same thing but len(a)'s meaning would be clear to beginners
print(string2.__len__())  # the same thing but would not be as clear
