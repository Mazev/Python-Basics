name = input()
godina = 1
ako_e_skasan = False
yspeh = 0

while godina <= 12:
    godishna_ocenka = float(input())
    if godishna_ocenka < 4:
        if ako_e_skasan:
            break
        ako_e_skasan = True
        continue
    yspeh += godishna_ocenka
    godina += 1

if ako_e_skasan:
    print(f'{name} has been excluded at {godina} grade')
else:
    print(f'{name} graduated. Average grade: {yspeh / 12:.2f}')
