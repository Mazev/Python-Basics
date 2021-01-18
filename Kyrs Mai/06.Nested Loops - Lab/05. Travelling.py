while True:
    line = input()
    if line == 'End':
        break
    deastination = line
    money_needed = float(input())
    save_money = 0
    while save_money < money_needed:
        curent_save_money = float(input())
        save_money += curent_save_money
    print(f"Going to {deastination}!")




