srok_dogovor = input()
tip_dogovor = input()
mob_internet = input()
broi_meseci = int(input())

taksa = 0
discont = 0
if srok_dogovor == 'one':
    if tip_dogovor == 'Small':
        taksa = 9.98
    elif tip_dogovor == 'Middle':
        taksa = 18.99
    elif tip_dogovor == 'Large':
        taksa = 25.98
    elif tip_dogovor == 'ExtraLarge':
        taksa = 35.99
elif srok_dogovor == 'two':
    if tip_dogovor == 'Small':
        taksa = 8.58
    elif tip_dogovor == 'Middle':
        taksa = 17.09
    elif tip_dogovor == 'Large':
        taksa = 23.59
    elif tip_dogovor == 'ExtraLarge':
        taksa = 31.79
    discont = 0.0375
if mob_internet == 'yes':
    if taksa <= 10:
        taksa += 5.50
    elif taksa <= 30:
        taksa += 4.35
    elif taksa > 30:
        taksa += 3.85
total_price = taksa * broi_meseci
total_price -= total_price * discont
print(f'{total_price:.2f} lv.')



