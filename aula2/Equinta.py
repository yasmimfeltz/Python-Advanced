"""
sets = só suportam elementos unicos
"""
# diferença de sets e dicionarios = os sets não receber um par de chave valores, só recebem valor
s1 = {1,2,3,4,5,6,}

for v in s1:
    print(v)

# outro jeito

s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)

print(s1)

s1 = set()
s1.update('Python')
print(s1)

# exemplo

s1 = {1,2,3,4,5,}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2

print(s3)
