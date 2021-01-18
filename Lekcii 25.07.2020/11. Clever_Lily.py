age = int(input())
praice_machin = float(input())
praice_toys = int(input())
money = 0
toys = 0
given_money = 10
for age in range(1, age +1):

    if age % 2 == 0:
        money += given_money - 1
        given_money += 10
    else:
        toys += 1

money += toys * praice_toys
if money >= praice_machin:
    left = money - praice_machin
    print(f'Yes! {left:.2f}')
else:
    need_money = praice_machin - money
    print(f'No! {need_money:.2f}')
#
# ages = int(input())
# laundry_price = float(input())
# toy_price = int(input())
# birthday_money = 10
# toys = 0
# total_money = 0
# for age in range(1, ages + 1):
#     if age % 2 == 0:
#         total_money += birthday_money - 1
#         birthday_money += 10
#     else:
#         toys += 1
# toys_money = toys * toy_price
# total_money += toys_money
# difference = abs(total_money - laundry_price)
# if total_money >= laundry_price:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")