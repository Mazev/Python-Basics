buget = int(input())
sezans = input()   #"Spring", "Summer", "Autumn" или "Winter"
fisharman_count = int(input())
praice = 0
if sezans == 'Spring':
    praice = 3000
    if fisharman_count <= 6:
        praice -= praice * 0.10
    elif 7 < fisharman_count <= 11 :
        praice -= praice * 0.15
    elif fisharman_count >12:
        praice -= praice * 0.25
elif sezans == 'Summer' or sezans == 'Autumn':
    praice = 4200
    if fisharman_count <= 6:
        praice -= praice * 0.10
    elif 7 < fisharman_count <= 11 :
        praice -= praice * 0.15
    elif fisharman_count >12:
        praice -= praice * 0.25
elif sezans == 'Winter':
    praice = 2600
    if fisharman_count <= 6:
        praice -= praice * 0.10
    elif 7 < fisharman_count <= 11 :
        praice -= praice * 0.15
    elif fisharman_count >12:
        praice -= praice * 0.25

if fisharman_count % 2 == 0 and sezans != "Autumn":
    praice -= praice * 0.05
money_needet = abs(buget - praice)
if buget > praice:
    print(f"Yes! You have {money_needet:.2f} leva left.")
else:
    print(f'"Not enough money! You need {money_needet:.2f} leva."')


