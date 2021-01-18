fuel = input()
cuontyti = float(input())
karta = input()
gasoline = 2.22
diesel = 2.33
gas = 0.93
praice = 0

if karta == 'Yes':
    if fuel == 'Gas':
        praice = (gas - 0.08) * cuontyti
    elif fuel == 'Gasoline':
        praice = (gasoline - 0.18) * cuontyti
    elif fuel == 'Diesel':
        praice = (diesel - 0.12) * cuontyti
else:
    if fuel == 'Gas':
        praice = gas * cuontyti
    elif fuel == 'Gasoline':
        praice = gasoline * cuontyti
    elif fuel == 'Diesel':
        praice = diesel * cuontyti
otstapka = 0
if 20 < cuontyti <= 25:
    otstapka = praice * 0.08
    total = praice - otstapka
    print(f'{total:.2f} lv.')
elif cuontyti > 25:
    otstapka = praice * 0.10
    total = praice - otstapka
    print(f'{total:.2f} lv.')
else:
    print(f'{praice:.2f} lv.')

























# if fuel == 'Gas':
#     if 20 < cuontyti >= 25:
#         praice = (gas - 0.08) * cuontyti
#     else:
#         praice = gas * cuontyti
# elif fuel == 'Gasoline':
#     if 20 < cuontyti >= 25:
#         praice = (gasoline - 0.18) * cuontyti
#     else:
#         praice = gasoline * cuontyti
# elif fuel == 'Diesel':
#     if 20 < cuontyti >= 25:
#         praice = (diesel - 0.12) * cuontyti
#     else:
#         praice = diesel * cuontyti
#
# if karta == 'Yes':
#     otstapka = praice * 0.10
#     total = praice - otstapka
#     print(f'{total:.2f} lv.')
# else:
#     print(f'{praice:.2f} lv.')