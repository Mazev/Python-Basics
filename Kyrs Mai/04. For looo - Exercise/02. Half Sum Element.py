import sys
n = int(input())
max_number = -sys.maxsize
sum_numbers = 0
for i in range(1, n +1):
    current_number = int(input())
    sum_numbers += current_number
    if current_number > max_number:
        max_number = current_number
total_sum = sum_numbers - max_number
if max_number == total_sum:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {abs(max_number - total_sum)}')