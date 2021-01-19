# while True :
#     num = input()
#     if num == 'Stop':
#         break
#     print(num)


# username = input()
# password = input()
# data = input()
# while data != password:
#     data = input()
#
# print(f'Welcome {username}!')


# num = int(input())
# sum = 0
# while sum < num:
#     sum += int(input())
# print(sum)

# n = int(input())
# counter = 1
# while counter <= n:
#     print(counter)
#     counter = 2 * counter + 1


i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i +=1
