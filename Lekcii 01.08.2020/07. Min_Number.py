from sys import maxsize

min_number = maxsize

line = input()

while line != 'Stop':
    curent_num = int(line)
    if curent_num < min_number:
        min_number = curent_num
    line = input()
print(min_number)



