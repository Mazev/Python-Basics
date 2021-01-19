budjet = float(input())
literst_benzin = float(input())
day = input()

praice_benzin = 2.10
praice_ekskurzovod = 100

mune_needet = literst_benzin * praice_benzin + praice_ekskurzovod
if day == 'Saturday':
    diskount = mune_needet * 0.10
elif day == 'Sunday':
    diskount = mune_needet * 0.20

total = mune_needet - diskount

if budjet > mune_needet:
    print(f'Safari time! Money left: {budjet - total:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total - budjet:.2f} lv.')