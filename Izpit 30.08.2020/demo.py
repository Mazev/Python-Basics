money_mashin = float(input())
laps = input()
fen_karta = input()
vid_kart = input()
money = 0
total = 0
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
    otstapka = money * 0.80

if fen_karta == 'no':

change = money_mashin - otstapka

    print(f"You bought {vid_kart} ticket for {laps} laps. Your change is {money_mashin - money:.2f}lv.")
else:
    print(f"You don't have enough money! You need {money - money_mashin:.2f}lv more.")
