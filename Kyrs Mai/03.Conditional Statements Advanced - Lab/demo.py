frut = input()
day = input()
kolichestvo = float(input())
praice = 0
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if frut == 'banana':
        praice = 2.50
    elif frut == 'apple':
        praice = 1.20
    elif frut == 'orange':
        praice = 0.85
    elif frut == 'grapefruit':
        praice = 1.45
    elif frut == 'kiwi':
        praice = 2.70
    elif frut == 'pineapple':
        praice = 5.50
    elif frut == 'grapes':
        praice = 3.85
if day == 'Saturday' or day == 'Sunday':
    if frut == 'banana':
        praice = 2.70
    elif frut == 'apple':
        praice = 1.25
    elif frut == 'orange':
        praice = 0.90
    elif frut == 'grapefruit':
        praice = 1.60
    elif frut == 'kiwi':
        praice = 3.00
    elif frut == 'pineapple':
        praice = 5.60
    elif frut == 'grapes':
        praice = 4.20
results = kolichestvo * praice
if results >0:
    print(f'{results:.2f}')
else:
    print('error')