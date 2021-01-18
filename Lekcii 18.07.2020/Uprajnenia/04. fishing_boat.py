badget = int(input())
sezon = input()
broi_ribari = int(input())

praice = 0
if sezon == 'Spring':
    praice += 3000
elif sezon == "Summer" or sezon == "Autumn":
    praice += 4200
elif sezon == 'Winter':
    praice += 2600
if broi_ribari <= 6:
    praice *= 0.90
elif 7 <= broi_ribari <= 11:
    praice *= 0.85
elif broi_ribari > 12:
    praice *= 0.75

if broi_ribari % 2 == 0 and sezon != "Autumn":
    praice *= 0.95
total = abs(praice - badget)

if badget >= praice:
    print(f"Yes! You have {total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total:.2f} leva.")
