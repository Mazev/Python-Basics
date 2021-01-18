age = int(input())
peralnq = float(input())
toys_praice = int(input())
money = 0
toys_count = 0
givet_money = 10
for age in range(1, age +1):
    if age % 2 == 0:
        money += givet_money - 1
        givet_money += 10
    else:
        toys_count += 1
toys_money = toys_count * toys_praice
total_money = money + toys_money
if total_money >= peralnq:
    print(f'Yes! {abs(total_money - peralnq):.2f}')
else:
    print(f'No! {abs(peralnq - total_money):.2f}')

