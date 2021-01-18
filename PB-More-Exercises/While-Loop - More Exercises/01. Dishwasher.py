botals = int(input())
preparat = botals * 750
needet_preparat = 0
counter_chinii = 0
counter_tendjeri = 0
counter = 0
pribori = input()
while True:
    counter += 1
    if pribori == 'End':
        break
    pribori = int(pribori)
    if counter % 3 != 0:
        needet_preparat = pribori * 5
        counter_chinii += pribori
        preparat -= pribori * 5
    elif counter % 3 == 0:
        needet_preparat = pribori * 15
        counter_tendjeri += pribori
    elif needet_preparat > preparat:
        print(f"Not enough detergent, {abs(preparat)} ml. more necessary!")
        preparat -= counter_tendjeri * 15
        break
    pribori = input()
if preparat > 0:
    print("Detergent was enough!")
    print(f"{counter_chinii} dishes and {counter_tendjeri} pots were washed.")
    print(f"Leftover detergent {preparat} ml.")
