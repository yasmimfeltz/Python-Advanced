print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
function range(start = 0, stop, step=1)
for in - repetition structure
"""
# continue - skip to the next loop
# break - ends the loop
# example 1
text = 'Python'
new_string = ''
for n, l in enumerate(text):
    print(n, l)

# example 2
for n in range(0, 100, 8):
    print(n)
print('##########')

for letter in text:
    if letter == 't':
        continue
        new_string = new_string + letter.upper()
    elif letter == 'h':
        new_string += letter.upper()
        break
    else:
        new_string += letter

        print(new_string)
