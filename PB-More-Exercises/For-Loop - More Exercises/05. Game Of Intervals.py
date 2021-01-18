hodove = int(input())

ot_0_do_9 = 0
ot_10_do_19 = 0
ot_20_do_29 = 0
ot_30_do_39 = 0
ot_40_do_50 = 0
invalid_number = 0
rezultat = 0
for i in range(hodove):
    num = int(input())
    if 0 <= num <= 9:
        ot_0_do_9 += 1
        rezultat += num * 0.20
    elif 10 <= num <= 19:
        ot_10_do_19 += 1
        rezultat += num * 0.30
    elif 20 <= num <= 29:
        ot_20_do_29 += 1
        rezultat += num * 0.40
    elif 30 <= num <= 39:
        ot_30_do_39 += 1
        rezultat += 50
    elif 40 <= num <= 50:
        ot_40_do_50 += 1
        rezultat += 100
    elif num <0 or num > 50:
        invalid_number += 1
        rezultat /= 2

print(f"{rezultat:.2f}")
print(f"From 0 to 9: {(ot_0_do_9 / hodove)* 100:.2f}%")
print(f"From 10 to 19: {(ot_10_do_19 / hodove) * 100:.2f}%")
print(f"From 20 to 29: {(ot_20_do_29 / hodove) * 100:.2f}%")
print(f"From 30 to 39: {(ot_30_do_39 / hodove) * 100:.2f}%")
print(f"From 40 to 50: {(ot_40_do_50 / hodove) * 100:.2f}%")
print(f"Invalid numbers: {(invalid_number / hodove) * 100:.2f}%")
