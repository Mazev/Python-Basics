floors = input()
num_floors = int(input())
bydget = float(input())

praice = 0

if floors == 'Roses':
    praice = 5.00 * num_floors
    if num_floors > 80:
        praice -= praice * 0.10
elif floors == 'Dahlias':
    praice = 3.80 * num_floors
    if num_floors > 90:
        praice -= praice * 0.15
elif floors == 'Tulips':
    praice = 2.80 * num_floors
    if num_floors > 80:
        praice -= praice * 0.10
elif floors == 'Narcissus':
    praice = 3.00 * num_floors
    if num_floors < 120:
        praice += praice * 0.15
elif floors == 'Gladiolus':
    praice = 2.50 * num_floors
    if num_floors < 80:
        praice += praice * 0.20

if bydget >= praice:
    print(f"Hey, you have a great garden with {num_floors} {floors} and {(bydget - praice):.2f} leva left.")
else:
    print(f"Not enough money, you need {(praice - bydget):.2f} leva more.")