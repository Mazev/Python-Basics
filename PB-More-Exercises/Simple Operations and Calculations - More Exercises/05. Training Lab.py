import math
w = float(input())

h = float(input())

daljina = h * 100 - 100
bura_na_red = math.floor(daljina / 70)
shirina = w * 100
bura_na_daljina = math.floor(shirina / 120)

obsht_broi = math.floor(bura_na_red * bura_na_daljina - 3)
print(f'{obsht_broi}')
