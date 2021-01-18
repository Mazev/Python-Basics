import math
holidays = int(input())

pochivni_dni = 127 * holidays
rabotni_dni = (365 - holidays) * 63
total_time_play = pochivni_dni + rabotni_dni
razlika = abs(30000 - total_time_play)


if total_time_play > 30000:
    print('Tom will run away')
    print(f'{math.floor(razlika / 60)} hours and {razlika % 60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{math.floor(razlika / 60)} hours and {razlika % 60} minutes less for play')