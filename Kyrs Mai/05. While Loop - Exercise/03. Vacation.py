money_needet = float(input())
have_money = float(input())
days = 0
spend_counter = 0
while True:
    command = input()
    money = float(input())
    days += 1
    if command == 'spend':
        if money > have_money:
            money = have_money
        have_money -= money
        spend_counter += 1
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f'{spend_counter}')
            break
    else:
        day_counter = 0
        have_money += money

        if have_money >= money_needet:
            print(f"You saved the money for {days} days.")
