"""
COUNT - ITERTOOLS
"""
from itertools import count

contador = count(start=5, step=0.1)

for valor in contador:
    print(round(valor,2))

    if valor >= 10 or valor <= -10:
        break 