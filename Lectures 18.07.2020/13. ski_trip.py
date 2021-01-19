days = float(input())
vid_staq = input()
ocenka = input()

nihts = days - 1
price = nihts

if vid_staq == 'room for one person':
    price *= 18
elif vid_staq == 'apartment':
    price *= 25
    if nihts < 10:
        price -= price * 0.30
    elif 10 <= nihts < 15:
        price -= price * 0.35
    elif nihts > 15:
        price -= price * 0.50
elif vid_staq == 'president apartment':
    price *= 35
    if nihts < 10:
        price -= price * 0.10
    elif 10 >= nihts <= 15:
        price -= price * 0.15
    elif nihts > 15:
        price -= price * 0.20
if ocenka == 'positive':
    price += price * 0.25
elif ocenka == 'negative':
    price -= price * 0.10
print(f'{price:.2f}')
