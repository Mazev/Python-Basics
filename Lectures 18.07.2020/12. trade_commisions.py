grad = input()
prodajba = float(input())

commisions = 0
if prodajba > 0:
    if grad == 'Sofia':
        if 0 <= prodajba <= 500:
            commisions = 0.05
        elif 500 <= prodajba <= 1000:
            commisions = 0.07
        elif 1000 <= prodajba <= 10000:
            commisions = 0.08
        elif prodajba > 10000:
            commisions = 0.12
        total = prodajba * commisions
        print(f'{total:.2f}')
    elif grad == 'Varna':
        if 0 <= prodajba <= 500:
            commisions = 0.045
        elif 500 <= prodajba <= 1000:
            commisions = 0.075
        elif 1000 <= prodajba <= 10000:
            commisions = 0.1
        elif prodajba > 10000:
            commisions = 0.13
        total = commisions * prodajba
        print(f'{total:.2f}')
    elif grad == 'Plovdiv':
        if 0 <= prodajba <= 500:
            commisions = 0.055
        elif 500 <= prodajba <= 1000:
            commisions = 0.08
        elif 1000 <= prodajba <= 10000:
            commisions = 0.12
        elif prodajba > 10000:
            commisions = 0.145
        total = commisions * prodajba
        print(f'{total:.2f}')
    else:
        print('error')
else:
    print('error')

