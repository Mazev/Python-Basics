num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
for number_1 in range(1, num_1 + 1):
    for number_2 in range(2, num_2 + 1):
        for number_3 in range(1 , num_3 + 1):
            if number_1 % 2 == 0:
                print(number_1)
            elif number_2 % 1 == 0:
                print(num_2)
            elif number_3 % 2 == 0:
                print(number_3)
