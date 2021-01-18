money_mashin = float(input())
laps = input()
fen_karta = input()
vid_kart = input()
money = 0
otstapka = money * 0.20
if laps == 'five':
    if vid_kart == 'Child':
        money = 7
    elif vid_kart == 'Junior':
        money = 9
    elif vid_kart == 'Adult':
        money = 12
    elif vid_kart == 'Profi':
        money = 18
if laps == 'ten':
    if vid_kart == 'Child':
        money = 11
    elif vid_kart == 'Junior':
        money = 16
    elif vid_kart == 'Adult':
        money = 21
    elif vid_kart == 'Profi':
        money = 32
if fen_karta == 'yes':
    if money_mashin > otstapka:
        change = money_mashin - otstapka
        print(f"You bought {vid_kart} ticket for {laps} laps. Your change is {change:.2f}lv.")
    elif money_mashin < otstapka:
        money = money_mashin - otstapka
        print(f"You don't have enough money! You need {money:.2f}lv more.")
else:
    if money_mashin > money:
        change = money_mashin - otstapka
        print(f"You bought {vid_kart} ticket for {laps} laps. Your change is {change:.2f}lv.")
    elif money_mashin < money:
        need_money = money_mashin - money
        print(f"You don't have enough money! You need {need_money:.2f}lv more.")




