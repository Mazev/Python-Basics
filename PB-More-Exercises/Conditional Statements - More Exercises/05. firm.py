import math

hours_needet = int(input())
have_days = int(input())
workers_count = int(input())

dni_za_obuchenie = have_days * 0.10
total_hours = (have_days - dni_za_obuchenie ) * 8
izvanredni_chasove = workers_count * (have_days * 2)
total = math.floor(total_hours + izvanredni_chasove)

if total > hours_needet:
    print(f'Yes!{total - hours_needet} hours left.')
else:
    print(f'Not enough time!{hours_needet - total} hours needed.')