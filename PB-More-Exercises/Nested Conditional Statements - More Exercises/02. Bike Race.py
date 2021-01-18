junior = int(input())
senior = int(input())
trase = input()

count_people = junior + senior
dopalnitelna_otstapka = 0
money = 0
if count_people <50:
    if trase == 'trail':
        money = junior * 5.50 + senior * 7
    elif trase == 'cross-country':
        money = junior * 8 + senior * 9.50
        if count_people >= 50:
            money = junior * 5.50 + senior * 7
            dopalnitelna_otstapka = money * 0.25
    elif trase == 'downhill':
        money = junior * 12.25 + senior * 13.75
    elif trase == 'road':
        money = junior * 20 + senior * 21.50
    razhodi = money * 0.05
    total = money - razhodi
    print(f'{total:.2f}')
if count_people >= 50:
    if trase == 'cross-country':
        money = (junior * 8 + senior * 9.50)
        dopalnitelna_otstapka = money * 0.25
        razhodi_1 = (money - dopalnitelna_otstapka) * 0.05
        total = money - dopalnitelna_otstapka - razhodi_1
        print(f'{total:.2f}')