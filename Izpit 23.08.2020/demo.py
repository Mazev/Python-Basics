mesec = input()
broi_chasove = int(input())
broi_hora = int(input())
vremeto_ot_denq = input()
cena_1_chovek = 0
otstapki_1 = 0

if mesec == "march" or mesec == "april" or mesec == "may":
    if vremeto_ot_denq == 'day':
        cena_1_chovek = 10.50
    elif vremeto_ot_denq == 'night':
        cena_1_chovek *= 8.40
elif broi_hora >= 4:
    otstapki_1 = cena_1_chovek * 0.90
    if broi_chasove >= 5:
        otstapki_1 *= 0.50
kraina_cena = otstapki_1 * broi_hora * broi_chasove
if mesec == "june" or mesec == "july" or mesec == "august":
    if vremeto_ot_denq == 'day':
        cena_1_chovek = 12.60
    elif vremeto_ot_denq == 'night':
        cena_1_chovek  = 10.20
elif broi_hora >= 4:
    otstapki_1 = cena_1_chovek * 0.90
elif broi_chasove >= 5:
    otstapki_1 *= 0.50
kraina_cena = otstapki_1 * broi_hora * broi_chasove
print(f'Price per person for one hour: {cena_1_chovek:.2f}')
print(f'Total cost of the visit: {kraina_cena:.2f}')
