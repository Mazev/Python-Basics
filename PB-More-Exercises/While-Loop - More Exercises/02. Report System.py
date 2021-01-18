money_colekt = float(input())
plashtane_broi = 0
counterna_plashtane_broi = 0
plashtane_karta = 0
counterna_plashtane_karta = 0
counter = 0
transaction = False
while money_colekt <= money_colekt:
    plashtane = input()
    counter +=1
    if plashtane == 'End':
        print('Failed to collect required money for charity.')
        break
    plashtane = float(plashtane)
    if counter % 2 == 1:     # плащане в брой повече от 100 само с карта , по малко от 10 само в брой
        if plashtane < 100:
            plashtane_broi += plashtane
            transaction = True
            counterna_plashtane_broi += 1
            print('Product sold!')
        elif plashtane >= 100:
            transaction = False
            print('Error in transaction!')
    elif counter % 2 == 0:    # плащане с карта по малко от 10 не , повече от  100 само с карта
        if plashtane > 10:
            plashtane_karta += plashtane
            transaction = True
            counterna_plashtane_karta += 1
            print('Product sold!')
        elif plashtane <= 10:
            transaction = False
            print('Error in transaction!')

    total = plashtane_karta + plashtane_broi
    if total >= money_colekt:
        print(f"Average CS: {plashtane_broi / counterna_plashtane_broi:.2f}")
        print(f"Average CC: {plashtane_karta / counterna_plashtane_karta:.2f}")
        break
