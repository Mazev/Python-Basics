import sys

max_num = -sys.maxsize

while True:
    curent_number = input()
    if curent_number == 'Stop':
        break
    num = int(curent_number)
    if num > max_num:
        max_num = num

print(max_num)



