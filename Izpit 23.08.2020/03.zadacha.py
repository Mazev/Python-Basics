# mesec = input()
# broi_chasove = int(input())
# broi_hora = int(input())
# vremeto_ot_denq = input()
# cena_1_chovek = 0
# otstapki_1 = 0
#
# if mesec == "march" or mesec == "april" or mesec == "may":
#     if vremeto_ot_denq == 'day':
#         cena_1_chovek = 10.50
#         if broi_hora >= 4:
#             otstapki_1 = cena_1_chovek * 0.90
#             if broi_chasove >= 5:
#                 otstapki_1 *= 0.50
#     elif vremeto_ot_denq == 'night':
#         cena_1_chovek *= 8.40
#         if broi_hora >= 4:
#             cena_1_chovek *= 0.90
#             if broi_chasove >= 5:
#                 cena_1_chovek *= 0.50
# kraina_cena = cena_1_chovek * broi_hora * broi_chasove
# if mesec == "june" or mesec == "july" or mesec == "august":
#     if vremeto_ot_denq == 'day':
#         cena_1_chovek = 12.60
#         if broi_hora >= 4:
#             otstapki_1 = cena_1_chovek * 0.90
#             if broi_chasove >= 5:
#                 otstapki_1 *= 0.50
#     elif vremeto_ot_denq == 'night':
#         cena_1_chovek  = 10.20
#         if broi_hora >= 4:
#             cena_1_chovek *= 0.90
#             if broi_chasove >= 5:
#                 cena_1_chovek *= 0.50
# kraina_cena = cena_1_chovek * broi_hora * broi_chasove
# print(f'Price per person for one hour: {cena_1_chovek:.2f}')
# print(f'Total cost of the visit: {kraina_cena:.2f}')


month = input()
hours_spent = int(input())
people_in_group = int(input())
time_of_day = input()
price_perhour_person = 0
if time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        price_perhour_person = 10.50
    elif month == "june" or month == "july" or month == "august":
        price_perhour_person = 12.60
else:
    if month == "march" or month == "april" or month == "may":
        price_perhour_person = 8.40
    elif month == "june" or month == "july" or month == "august":
        price_perhour_person = 10.20

if people_in_group >= 4:
    price_perhour_person = price_perhour_person - (price_perhour_person * 0.90)

if hours_spent >= 5:
    price_perhour_person = price_perhour_person - (price_perhour_person /2)

full_price = price_perhour_person * people_in_group * hours_spent

print(f"Price per person for one hour: {price_perhour_person:.2f}")
print(f"Total cost of the visit: {full_price:.2f}")