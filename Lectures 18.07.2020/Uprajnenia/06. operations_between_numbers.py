n_1 = int(input())
n_2 = int(input())
operator = input()

rezult = 0
vid = ''
if operator == '+':
    rezult = n_1 + n_2
    if rezult % 2 == 0:
        vid = 'even'
    else:
        vid = 'odd'
    print(f"{n_1} {operator} {n_2} = {rezult} - {vid}")
elif operator == '-':
    rezult = n_1 - n_2
    if rezult % 2 == 0:
        vid = 'even'
    else:
        vid = 'odd'
    print(f"{n_1} {operator} {n_2} = {rezult} - {vid}")
elif operator == '*':
    rezult = n_1 * n_2
    if rezult % 2 == 0:
        vid = 'even'
    else:
        vid = 'odd'
    print(f"{n_1} {operator} {n_2} = {rezult} - {vid}")
elif operator == '/':
    if n_2 == 0:
        print(f"Cannot divide {n_1} by zero")
    else:
        rezult = n_1 / n_2
        print(f"{n_1} / {n_2} = {rezult:.2f}")


elif operator == '%':
    if n_2 == 0:
        print(f"Cannot divide {n_1} by zero")
    else:
        rezult = n_1 % n_2
        print(f"{n_1} % {n_2} = {rezult}")

    # if rezult == 0:
    #     print(f"Cannot divide {n_1} by zero")


