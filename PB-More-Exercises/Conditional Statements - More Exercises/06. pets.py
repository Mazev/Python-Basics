import math
days = int(input())
food = int(input())
dogs = float(input())
cat = float(input())
tortol = float(input())

dog_food = dogs * days
cat_food = cat * days
tortol_food = tortol * days
total = dog_food + cat_food + tortol_food / 1000

if total < food:
    print(f"{math.floor(food - total)} kilos of food left.")
else:
    print(f'{math.ceil(total - food)} more kilos of food are needed.')