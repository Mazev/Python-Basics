import sys
n = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize
for i in range(n):
    curent_number = int(input())
    if curent_number > max_number:
        max_number = curent_number
    elif curent_number < min_number:
        min_number = curent_number
print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
