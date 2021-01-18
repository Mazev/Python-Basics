budget = float(input())
sezon = input()

praise = 0
nastanqvane = ''
lokacia = ''

if budget <= 1000:
    nastanqvane = 'Camp'
    if sezon == 'Summer':
        lokacia = 'Alaska'
        praise = budget * 0.65
    elif sezon == 'Winter':
        lokacia = 'Morocco'
        praise = budget * 0.45
elif 1000 < budget <= 3000:
    nastanqvane = 'Hut'
    if sezon == 'Summer':
        lokacia = 'Alaska'
        praise = budget * 0.80
    elif sezon == 'Winter':
        lokacia = 'Morocco'
        praise = budget * 0.60
elif budget > 3000:
    nastanqvane = 'Hotel'
    if sezon == 'Summer':
        lokacia = 'Alaska'
        praise = budget * 0.90
    elif sezon == 'Winter':
        lokacia = 'Morocco'
        praise = budget * 0.90
print(f'{lokacia} - {nastanqvane} - {praise:.2f}')
