city = input()
prodajbi = float(input())

komisionna = 0
if prodajbi > 0:
    if city == 'Sofia':
        if 0 <= prodajbi <= 500:
            komisionna = prodajbi * 0.05
        elif 500 <= prodajbi <= 1000:
            komisionna = prodajbi * 0.07
        elif 1000 <= prodajbi <= 10000:
            komisionna = prodajbi *0.08
        elif prodajbi > 10000:
            komisionna = prodajbi * 0.12
        print(f'{komisionna:.2f}')
    elif city == 'Varna':
        if 0 <= prodajbi <= 500:
            komisionna = prodajbi * 0.045
        elif 500 <= prodajbi <= 1000:
            komisionna = prodajbi * 0.075
        elif 1000 <= prodajbi <= 10000:
            komisionna = prodajbi * 0.10
        elif prodajbi > 10000:
            komisionna = prodajbi * 0.13
        print(f'{komisionna:.2f}')
    elif city == 'Plovdiv':
        if 0 <= prodajbi <= 500:
            komisionna = prodajbi * 0.055
        elif 500 <= prodajbi <= 1000:
            komisionna = prodajbi * 0.08
        elif 1000 <= prodajbi <= 10000:
            komisionna = prodajbi * 0.12
        elif prodajbi > 10000:
            komisionna = prodajbi * 0.145
        print(f'{komisionna:.2f}')
    else:
        print('error')
else:
    print('error')