n = int(input())
l = int(input())

for num_1 in range(1, n + 1):
    for num_2 in range(1, n + 1):
        for num_3 in range(ord('a'), ord('a') + l):
            for num_4 in range(ord('a'), ord('a') + l):
                for num_5 in range(1, n + 1):
                    if num_1 < num_5 > num_1:
                        print(f'{num_1}{num_2}{chr(num_3)}{chr(num_4)}{num_5}', end=' ')

