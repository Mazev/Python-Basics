# for num in range(1,1000):
#     if num % 10 == 7:
#         print(num)


# import sys
# n = int(input())
#
# max_element = - sys.maxsize
# sum_numbers = 0
#
# for num in range(1, n ):
#     number = int(input())
#     if max_element < number:
#         max_element = number
#     sum_numbers += number
#
# sum_numbers -= max_element
#
# if sum_numbers == max_element:
#     print('Yes')
#     print(f'Sum = {sum_numbers}')
# else:
#     print('No')
#     print(f'Diff = {abs(sum_numbers - max_element)}')


# import sys
# n = int(input())
# odd_sum = 0
# even_sum = 0
# min_odd = sys.maxsize
# min_even = sys.maxsize
# max_odd = - sys.maxsize
# max_even = -sys.maxsize
# for number in range(1, n + 1):
#     curent_number = float(input())
#     if number % 2 == 0:
#         even_sum += curent_number
#         if curent_number > max_even:
#             max_even = curent_number
#         if curent_number < min_even:
#             min_even = curent_number
#     else:
#         odd_sum += curent_number
#         if curent_number > max_odd:
#             max_odd = curent_number
#         if curent_number < min_odd:
#             min_odd = curent_number
# print(f'OddSum={odd_sum:.2f},')
# if min_odd == sys.maxsize:
#     print("OddMin=No,")
# else:
#     print(f"OddMin={min_odd:.2f},")
# if max_odd == -sys.maxsize:
#     print("OddMax=No,")
# else:
#     print(f"OddMax={max_odd:.2f},")
# print(f"EvenSum={even_sum:.2f},")
# if min_even == sys.maxsize:
#     print("EvenMin=No,")
# else:
#     print(f"EvenMin={min_even:.2f},")
# if max_even == -sys.maxsize:
#     print("EvenMax=No")
# else:
#     print(f"EvenMax={max_even:.2f}")