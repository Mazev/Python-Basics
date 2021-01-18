while True:
    distination = input()
    if distination == 'End':
        break
    money_needet = int(input())
    budget = 0
    while budget < money_needet:
        budget += int(input())
    print(f'Going to {distination}!')