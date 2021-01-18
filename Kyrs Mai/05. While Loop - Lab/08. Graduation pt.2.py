name = input()
godishna_ocenka = float(input())
zbor_ocenki = 0.00
broqch = 0
slabi_ocenki = 0
while broqch <= 12:
    if godishna_ocenka < 4 :
        slabi_ocenki +=1
        if slabi_ocenki ==2:
            break
    zbor_ocenki += godishna_ocenka
    broqch += 1

if slabi_ocenki == 2:
    print(f"{name} has been excluded at {broqch} grade")
else:
    print(f"{name} graduated. Average grade: {zbor_ocenki / broqch:.2f}")


# name = input()
# godina = 1
# ako_e_skasan = False
# yspeh = 0
#
# while godina <= 12:
#     godishna_ocenka = float(input())
#     if godishna_ocenka < 4:
#         if ako_e_skasan:
#             break
#         ako_e_skasan = True
#         continue
#     yspeh += godishna_ocenka
#     godina += 1
#
# if ako_e_skasan:
#     print(f'{name} has been excluded at {godina} grade')
# else:
#     print(f'{name} graduated. Average grade: {yspeh / 12:.2f}')