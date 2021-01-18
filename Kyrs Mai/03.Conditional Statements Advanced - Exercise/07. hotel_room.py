month = input()    #May, June, July, August, September или October
days_count = int(input())

studio_praice = 0
apartment_praice = 0
if month == 'May' or month == 'October':
    studio_praice = days_count * 50
    apartment_praice = days_count * 65
    if days_count <=7:
        studio_praice -= studio_praice * 0.05
    elif days_count > 14:
        studio_praice -= studio_praice * 0.30
        apartment_praice -= apartment_praice * 0.10
elif month == 'June' or month == 'September':
    studio_praice = days_count * 75.20
    apartment_praice = days_count * 68.70
    if days_count > 14:
        studio_praice -= studio_praice * 0.20
        apartment_praice -= apartment_praice * 0.10
elif month == 'July' or month == 'August':
    studio_praice = days_count * 76
    apartment_praice = days_count * 77
    if days_count > 14:
        apartment_praice -= apartment_praice * 0.10
print(f"Apartment: {apartment_praice:.2f} lv.")
print(f"Studio: {studio_praice:.2f} lv.")
