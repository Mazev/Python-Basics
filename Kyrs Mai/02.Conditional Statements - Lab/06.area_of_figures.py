import math
figures = input()

if figures == 'square':
    a = float(input())
    print(f'{a * a:.3f}')
elif figures == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a * b:.3f}')
elif figures == 'circle':
    a = float(input())
    print(print(f"{math.pi * a **2:.3f}"))
elif figures == 'triangle':
    a = float(input())
    b = float(input())
    print((f"{(a * b)/2:.3f}"))
