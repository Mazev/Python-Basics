puzzle = 2.60
kukla = 3
bear = 4.10
minion = 8.20
truck = 2

trip_price = float(input())
puzzle_count = int(input())
kukla_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_total = puzzle * puzzle_count
kukla_total = kukla * kukla_count
bear_total = bear * bear_count
minion_total = minion * minion_count
truck_total = truck * truck_count

toys_total_price = puzzle_total + kukla_total + bear_total + minion_total + truck_total
toys_total_count = puzzle_count + kukla_count + bear_count + minion_count + truck_count

if toys_total_count >= 50:
    toys_price = toys_total_price - (toys_total_price * 0.25)
else:
    toys_price = toys_total_price

money_left = toys_price - (toys_price * 0.10)

if money_left >= trip_price:
    left = money_left - trip_price
    print(f"Yes! {left:.2f} lv left.")
else:
    needed = trip_price - money_left
    print(f"Not enough money! {needed:.2f} lv needed.")