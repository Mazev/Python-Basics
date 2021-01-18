budget = float(input())
vid_tikets = input()
number_pepals = int(input())

vip_tiket = 499.99
normal_tiket = 249.99
transport = 0
tiket_praice = 0

if vid_tikets == 'VIP':
    if 1 <= number_pepals <= 4:
        tiket_praice = number_pepals * vip_tiket
        transport = budget * 0.75
    elif 5 <= number_pepals <= 9:
        tiket_praice = number_pepals * vip_tiket
        transport = budget * 0.60
    elif 10 <= number_pepals <= 24:
        tiket_praice = number_pepals * vip_tiket
        transport = budget * 0.50
    elif 25 <= number_pepals <= 49:
        tiket_praice = number_pepals * vip_tiket
        transport = budget * 0.40
    elif number_pepals >= 50:
        tiket_praice = number_pepals * vip_tiket
        transport = budget * 0.25
elif vid_tikets == 'Normal':
    if 1 <= number_pepals <= 4:
        transport = budget * 0.75
        tiket_praice = number_pepals * normal_tiket
    elif 5 <= number_pepals <= 9:
        tiket_praice = number_pepals * normal_tiket
        transport = budget * 0.60
    elif 10 <= number_pepals <= 24:
        tiket_praice = number_pepals * normal_tiket
        transport = budget * 0.50
    elif 25 <= number_pepals <= 49:
        tiket_praice = number_pepals * normal_tiket
        transport = budget * 0.40
    elif number_pepals >= 50:
        tiket_praice = number_pepals * normal_tiket
        transport = budget * 0.25

money_left= budget - transport

if money_left > tiket_praice:
    print(f'Yes! You have {money_left - tiket_praice:.2f} leva left.')
else:
    print(f'Not enough money! You need {tiket_praice - money_left:.2f} leva.')
