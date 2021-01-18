botals = int(input())
preparat = botals * 750
counter_chinii = 0
counter_tendjeri = 0
counter = 0
while preparat >=0:
    pribori = input()
    counter += 1
    if pribori == 'End':
        break
    pribori = int(pribori)
    if counter % 3 == 0:
        counter_tendjeri += pribori
        preparat -= counter_tendjeri * 15
    preparat -= pribori * 5
    counter_chinii += pribori

if preparat > 0:
    print("Detergent was enough!")
    print(f"{counter_chinii} dishes and {counter_tendjeri} pots were washed.")
    print(f"Leftover detergent {preparat} ml.")
else:
    print(f"Not enough detergent, {abs(preparat)} ml. more necessary!")


