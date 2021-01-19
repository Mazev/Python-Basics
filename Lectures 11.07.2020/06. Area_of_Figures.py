import math

figures = input()

if figures == "square":
    side_1 = float(input())
    print(f"{side_1 * side_1:.3f}")
elif figures == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    print(f"{side_1 * side_2:.3f}")
elif figures == "circle":
    side_1 = float(input())
    print(f"{math.pi * side_1**2:.3f}")
elif figures == "triangle":
    side_1 = float(input())
    side_2 = float(input())
    print(f"{(side_1 * side_2)/2:.3f}")