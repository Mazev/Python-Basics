sezon = input()
kilometri = float(input())

meseci = 4
zaplata = 0

if kilometri <= 5000:
    if sezon == 'Spring' or sezon == 'Autumn':
        zaplata = kilometri * 0.75
    elif sezon == 'Summer':
        zaplata = kilometri * 0.90
    elif sezon == 'Winter':
        zaplata = kilometri * 1.05
elif 5000 < kilometri <= 10000:
    if sezon == 'Spring' or sezon == 'Autumn':
        zaplata = kilometri * 0.95
    elif sezon == 'Summer':
        zaplata = kilometri * 1.10
    elif sezon == 'Winter':
        zaplata = kilometri * 1.25
else:
    if sezon == 'Spring' or sezon == 'Autumn' or sezon == 'Sumer' or sezon == 'Winter':
        zaplata = kilometri * 1.45
zaplata = zaplata * meseci
danaci = zaplata *0.10
total = zaplata - danaci
print(f'{total:.2f}')