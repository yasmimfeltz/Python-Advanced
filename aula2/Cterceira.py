print("▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀NEW CLASS▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
"""
tuplas em python
"""
t1 = (1,2,3, 'K', 'Yasmim Kalfeltz')
# print(t1[4])
for v in t1:
    print(v)

t1 = 1,2,'Yasmim',4,5
t2 = 6,7,8,9,10
t3 = t1 + t2

n1, n2, n3, *_ = t3
print(n3)

t1 = (1,2,'Yasmim',4,5) * 20

print(t1)

t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 3000

print(t1)