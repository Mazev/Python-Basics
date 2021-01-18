import sys
min_number = sys.maxsize
while True:
    line = input()
    if line == 'Stop':
        break
    curerent_number = int(line)
    if curerent_number < min_number:
        min_number = curerent_number
print(min_number)
