# Декорът за филма е на стойност 10% от бюджета.
# При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

buget_film = float(input())
count_statist = int(input())
praice_dres = float(input())

dekor = buget_film * 0.10
total_praice_dres =  praice_dres * count_statist
total = 0
if count_statist >= 150:
    discount_dres = total_praice_dres * 0.10
    total_praice_dres -= discount_dres
    total = dekor + total_praice_dres
else:
    total = dekor + total_praice_dres

if total > buget_film:
    print(f'Not enough money!')
    print(f'Wingard needs {total - buget_film:.2f} leva more.')
else:
    print(f"Action!")
    print(f"Wingard starts filming with {buget_film - total:.2f} leva left.")
