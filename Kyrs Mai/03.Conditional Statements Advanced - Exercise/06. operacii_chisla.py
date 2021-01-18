n1 = int(input())
n2 = int(input())
operator = input()   #"+", "-", "*", "/", "%".
rezult = 0
vid = ''
if operator == '+' or operator == '-' or operator == '*':
    if operator == '+':
        rezult = n1 + n2
    elif operator == '-':
        rezult = n1 - n2
    elif operator == '*':
        rezult = n1 * n2
    if rezult % 2 == 0:
       vid = 'even'
    else:
        vid = 'odd'
    print(f"{n1} {operator} {n2} = {rezult} - {vid}")
if operator == '/':
    if n2 != 0:
        rezult = n1 / n2
        print(f"{n1} / {n2} = {rezult:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")

elif operator == '%':
    if n2 != 0:
        rezult = n1 / n2
        print(f"{n1} % {n2} = {rezult:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")




