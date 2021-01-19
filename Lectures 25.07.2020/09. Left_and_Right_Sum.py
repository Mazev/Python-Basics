n = int(input())
left_sum = 0
for i in range(n):
    left_sum = left_sum + int(input())
raith_sum = 0
for i in range (n):
    raith_sum = raith_sum + int(input())

if left_sum == raith_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(raith_sum - left_sum)
    print(f'No, diff = {diff}')