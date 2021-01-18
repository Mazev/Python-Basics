# furst_num = int(input())
# second_num =int (input())
# for number in range(furst_num, second_num + 1):
#     number_to_str = str(number)
#     even_sum = 0
#     odd_sum = 0
#     for index, digit in enumerate(number_to_str):
#         if index % 2 == 0:
#             even_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#     if even_sum == odd_sum:
#         print(number, end = ' ')
# print()


first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    number = str(number)
    for digit in range(0, 6):
        if digit % 2 == 0:
            sum_of_odd_numbers += int(number[digit])
        else:
            sum_of_even_numbers += int(number[digit])
    if sum_of_even_numbers == sum_of_odd_numbers:
        print(number, end=" ")