month = input()
noshtuvki = int(input())

studio_rent = 0
apartment_rent = 0
if month == 'May' or month == 'October':
    studio_rent = 50 * noshtuvki
    apartment_rent = 65 * noshtuvki
    if noshtuvki > 14:
        studio_rent -= studio_rent * 0.30
        apartment_rent -= apartment_rent * 0.10
    elif noshtuvki > 7:
        studio_rent -= studio_rent * 0.05
elif month == 'June' or month == 'September':
    studio_rent = 75.20 * noshtuvki
    apartment_rent = 68.70 * noshtuvki
    if noshtuvki > 14:
        studio_rent -= studio_rent * 0.20
        apartment_rent -= apartment_rent * 0.10
elif month == 'Jule' or month == 'August':
    studio_rent = 76 * noshtuvki
    apartment_rent = 77 * noshtuvki
    if noshtuvki > 14:
        apartment_rent -= apartment_rent * 0.10
print(f'Apartment: {apartment_rent:.2f} lv.')
print(f'Studio: {studio_rent:.2f} lv.')
