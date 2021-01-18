num = int(input())
total_sum = 0
for i in range(num):
    numbers = int(input())
    total_sum += numbers
print(f'{total_sum / num:.2f}')