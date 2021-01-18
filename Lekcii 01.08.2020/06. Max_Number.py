from sys import maxsize
max_number = - maxsize
num = input()

while num != "Stop":
    curent_num = int(num)
    if curent_num > max_number:
        max_number = curent_num
    num = input()
print(max_number)
