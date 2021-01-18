screening_type = input()
rows = int(input())
colums = int(input())

cinema_capacity = rows * colums
income = 0
if screening_type == 'Premiere':
    income = cinema_capacity * 12
elif screening_type == 'Normal':
    income = cinema_capacity * 7.50
elif screening_type == 'Discount':
    income = cinema_capacity * 5.00
print(f'{income:.2f} leva')
