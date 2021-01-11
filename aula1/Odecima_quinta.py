print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
# interando com strings usando while
phrase = 'o rato roeu a roupa do rei de roma'
sentence_size = len(phrase)
counter = 0
new_string = ''

while counter < sentence_size:
    letter = phrase[counter]
    if letter == 'r':
        new_string += 'r'
        new_string += 'R'

    else:
        new_string += letter
    counter += 1

print(new_string)