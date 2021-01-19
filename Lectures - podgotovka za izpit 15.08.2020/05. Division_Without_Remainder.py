n = int(input())
p1 = 0
p2 = 0
p3 = 0
for index in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1
procent_1 = (p1/ n) * 100
procent_2 = (p2/ n) * 100
procent_3 = (p3/ n) * 100
print(f'{procent_1:.2f}%')
print(f'{procent_2:.2f}%')
print(f'{procent_3:.2f}%')