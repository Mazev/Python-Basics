num_students = int(input())

obsht_yspeh = 0
top_students = 0
mejdu_4_i_5 = 0
mejdu_3_i_4 = 0
skasani = 0
for i in range(num_students):
    ocenki = float(input())
    obsht_yspeh += ocenki
    if ocenki >= 5.00:
        top_students += 1
    elif 4.00 <= ocenki <= 4.99:
        mejdu_4_i_5 += 1
    elif 3.00 <= ocenki <= 3.99:
        mejdu_3_i_4 += 1
    elif ocenki < 3:
        skasani += 1

sreden_yspeh = obsht_yspeh / num_students

print(f"Top students: {(top_students / num_students) * 100 :.2f}%")
print(f"Between 4.00 and 4.99: {(mejdu_4_i_5 / num_students) * 100 :.2f}%")
print(f"Between 3.00 and 3.99: {(mejdu_3_i_4 / num_students)* 100:.2f}%")
print(f"Fail: {(skasani / num_students)*100:.2f}%")
print(f"Average: {sreden_yspeh:.2f}")
