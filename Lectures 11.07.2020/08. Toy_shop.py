trip = float(input())
puzzel = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
truck = int(input())
puzzel_price = 2.60
dolls_price = 3
bears_price = 4.10
minions_price = 8.20
trucks_price = 2
all_sales = puzzel * puzzel_price + dolls * dolls_price + bears * bears_price + minions * minions_price + truck * trucks_price
count_toys = puzzel + dolls + bears + minions + truck
if count_toys >= 50:
    discount = all_sales * 0.25
    final_price = all_sales - discount
    rent = final_price * 0.1
    profit = final_price - rent
    print(f'Yes! {profit - trip :.2f} lv left.')
if all_sales < 50:
    rent = all_sales * 0.1
    profit = all_sales - rent
    print(f'Not enough money! {profit - trip:.2f} lv needed.')