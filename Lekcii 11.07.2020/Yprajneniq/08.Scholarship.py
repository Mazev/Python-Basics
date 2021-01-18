import math
dohod = float(input())
middle_grade = float(input())
min_salary = float(input())


social_scholarship = math.floor(min_salary * 0.35)
excellent_scholarship = math.floor(middle_grade * 25)


if middle_grade >= 5.50:
    if dohod < min_salary and middle_grade > excellent_scholarship:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    elif excellent_scholarship > social_scholarship:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif middle_grade > 4.50:
    if dohod < min_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")





# if dohod >= 450 and sreden_uspeh < 5.50:
#     print('You cannot get a scholarship!')
# elif dohod >= 450 and sreden_uspeh > 4.50:
#     print(f"You get a Social scholarship {stependiq} BGN")
# elif sreden_uspeh >= 5.50:
#     print(f'You get a scholarship for excellent results {stependiq} BGN')
# elif stependiq > sreden_uspeh:
#     print(f"You get a Social scholarship {stependiq} BGN")


#
# income = float(input())
# middle_grade = float(input())
# min_salary = float(input())

# social_scholarship = floor(min_salary * 0.35)
# excellent_scholarship = floor(middle_grade * 25)

# if middle_grade >= 5.50:
#     if income < min_salary and social_scholarship > excellent_scholarship:
#         print(f"You get a Social scholarship {social_scholarship} BGN")
#     elif excellent_scholarship >= social_scholarship:
#         print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
#     else:
#         print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
# elif middle_grade > 4.50:
#     if income < min_salary:
#         print(f"You get a Social scholarship {social_scholarship} BGN")
#     else:
#         print("You cannot get a scholarship!")
# else:
#     print("You cannot get a scholarship!")