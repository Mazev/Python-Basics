fruit = input()
day = input()
quantuty = float(input())
praice = 0
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day =='Friday':
    if fruit == 'banana':
        praice = 2.50
    elif fruit == 'apple':
        praice = 1.20
    elif fruit == 'orange':
        praice = 0.85
    elif fruit == 'grapefruit':
        printe = 1.45
    elif fruit == 'kiwi':
        praice = 2.70
    elif fruit == 'pineapple':
        praice = 5.50
    elif fruit == 'grapes':
        praice = 3.85
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        praice = 2.70
    elif fruit == 'apple':
        praice = 1.25
    elif fruit == 'orange':
        praice = 0.90
    elif fruit == 'grapefruit':
        printe = 1.60
    elif fruit == 'kiwi':
        praice = 3.00
    elif fruit == 'pineapple':
        praice = 5.60
    elif fruit == 'grapes':
        praice = 4.20
total = praice * quantuty
if quantuty > 0:
    print(f'{total:.2f}')
else:
    print('error')
