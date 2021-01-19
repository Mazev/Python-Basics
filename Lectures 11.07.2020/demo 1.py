import math

vid_figura = input()

if "square" == vid_figura:
    area_1 = float(input())
    print(f"{area_1 * area_1:.3f}")
elif "rectangle" == vid_figura:
    area_1 = float(input())
    area_2 = float(input())
    print(f"{area_1 * area_2:.3f}")
elif "circle" == vid_figura:
    area_1 = float(input())
    print(f"{math.pi * area_1 ** 2:.3f}")
elif "triangle" == vid_figura:
    area_1 = float(input())
    area_2 = float(input())
    print(f"{area_1 * area_2 / 2:.3f}")
