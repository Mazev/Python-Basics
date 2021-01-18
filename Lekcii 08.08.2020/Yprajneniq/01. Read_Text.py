# n= int(input())
# current = 1
# is_current_is_biger_then_n = False
# for row in range(1, n + 1):
#     for col in range(1, row + 1):
#         if current > n:
#             is_current_is_biger_then_n = True
#             break
#         print(str(current), ' ', end='')
#         current += 1
#     if is_current_is_biger_then_n:
#         break
#     print()

n = int(input())
current = 1
is_current_is_biger_then_n = False
for x in range(1, n+1):
    for y in range(1, x +1):
        if current > n:
            is_current_is_biger_then_n = True
            break
        print(str(current) + '', end = ' ')
        current += 1
    if is_current_is_biger_then_n:
        break
    print()