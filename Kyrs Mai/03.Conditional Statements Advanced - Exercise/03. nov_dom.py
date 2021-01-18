flowers = input()  #"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flowers_count = int(input())
budget = int(input())
praice = 0
if flowers == 'Roses':
    praice = 5
    if flowers_count > 80:
        praice -= praice * 0.10
elif flowers == 'Dahlias':
    praice = 3.80
    if flowers_count > 90:
        praice -= praice * 0.15
elif flowers == 'Tulips':
    praice = 2.80
    if flowers_count > 80:
        praice -= praice * 0.15
elif flowers == 'Narcissus':
    praice = 3
    if flowers_count < 120:
        praice += praice * 0.15
elif flowers == 'Gladiolus':
    praice = 2.50
    if flowers_count < 80:
        praice += praice * 0.20
total = flowers_count * praice
if budget >= total:
    left = budget - total
    print(f"Hey, you have a great garden with {flowers_count} {flowers} and {left:.2f} leva left.")
else:
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
