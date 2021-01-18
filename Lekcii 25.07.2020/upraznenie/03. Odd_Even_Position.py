import sys
n = int(input())
sum_odd = 0
sum_even = 0
min_odd = sys.maxsize
min_even = sys.maxsize
max_odd = - sys.maxsize
max_even = - sys.maxsize
for number in range(1, n + 1):
    curent_number = float(input())
    if number % 2 == 0:
        sum_even += curent_number
        if curent_number > max_even:
            max_even = curent_number
        if curent_number < min_even:
            min_even = curent_number
    else:
        sum_odd += curent_number
        if curent_number > max_odd:
            max_odd = curent_number
        if curent_number < min_odd:
            min_odd = curent_number
print(f"OddSum={sum_odd:.2f},")
if min_odd == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")
if max_odd == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")
print(f"EvenSum={sum_even:.2f},")
if min_even == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")
if max_even == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")

