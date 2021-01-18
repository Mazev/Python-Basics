import math
area = int(input())
ot_1_kvadraten_metar = float(input())
need_liters = int(input())
workers = int(input())

total_greeps = area * ot_1_kvadraten_metar
vino = (total_greeps / 2.50) / 100 * 40
if need_liters > vino:
    print(f'It will be a tough winter! More {math.floor(need_liters - vino)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(vino)} liters.')
    print(f'{math.floor(vino - need_liters)} liters left -> {math.floor((vino - need_liters)/ workers)} liters per person.')