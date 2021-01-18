kapcitet_stdion = int(input())
num_fenove = int(input())
sektor_a = 0
sektor_b = 0
sektor_v = 0
sektor_g = 0
fenove = 0
for i in range(kapcitet_stdion):
    fenove += 1
    gosti = input()
    if gosti == 'A':
        sektor_a += 1
    elif gosti == 'B':
        sektor_b += 1
    elif gosti == 'V':
        sektor_v += 1
    elif gosti == 'G':
        sektor_g += 1
    if fenove == num_fenove:
        break


print(f'{(sektor_a / num_fenove) * 100:.2f}%')
print(f'{(sektor_b / num_fenove) * 100:.2f}%')
print(f'{(sektor_v / num_fenove) * 100:.2f}%')
print(f'{(sektor_g / num_fenove) * 100:.2f}%')
print(f'{(fenove / kapcitet_stdion) * 100:.2f}%')
