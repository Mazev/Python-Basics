n = int(input())
raith_saiz = 0
left_saiz = 0
for i in range(n):
    current_number = int(input())
    raith_saiz += current_number
for i in range(n):
    current_number = int(input())
    left_saiz += current_number

if raith_saiz == left_saiz:
    print(f'Yes, sum = {raith_saiz}')
else:
    print(f'No, diff = {abs(raith_saiz - left_saiz)}')