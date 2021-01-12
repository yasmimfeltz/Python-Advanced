print('▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀')
"""
python lists
Slicing
append, insert, pop, del, clear, extend, +
min, max
range
"""
#        0    1    2    3    4    5
list = ['A', 'B', 'C', 'D', 'E', 10.5]
list[5] = 'something.'

print(list[5])
print(list[0:3])
print(list[:3])
print(list[::2])
print(list[::-1])

# example 2
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.append('b')
l1.extend(l2)
l2.insert(0, 'monkey')
l3 = l1 + l2

print(l2[0])
print(l1)

# example 3
l2 = [4,5,6]
print(l2)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)