budget = float(input())
total = 0
product_count = 0
product_name = input()
while product_name != 'Stop':
    praice = float(input())
    product_count += 1
    if product_count % 3 == 0:
        praice /= 2

    if (total + praice) > budget:
        print(f"You don't have enough money!")
        print(f'You need {abs((praice + total) - budget):.2f} leva!')
        break
    total+= praice
    product_name = input()

if product_name == 'Stop':
    print(f'You bought {product_count} products for {total:.2f} leva.')
