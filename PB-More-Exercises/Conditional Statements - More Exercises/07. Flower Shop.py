import math
count_magnolii = int(input())
count_zumbuli = int(input())
count_rozi = int(input())
count_kaktusi = int(input())
podarak = float(input())

magnolii = 3.25
zumbuli = 4
rozi = 3.50
kaktusi = 8

all_floors = count_magnolii * magnolii + count_zumbuli * zumbuli + count_rozi * rozi + count_kaktusi * kaktusi
otstapka = all_floors * 0.05
total = all_floors - otstapka

if total > podarak:
    print(f'She is left with {math.floor(total - podarak)} leva.')
else:
    print(f'She will have to borrow {math.ceil(podarak - total)} leva.')