# цената на малините е на половина по-ниска от тази на ягодите;
#  цената на портокалите е с 40% по-ниска от цената на малините;
#  цената на бананите е с 80% по-ниска от цената на малините.

strobere_praice = float(input())
bananas_kg = float(input())
orange_kg = float(input())
malini_kg = float(input())
stroberes_kg = float(input())


praice_malini = strobere_praice / 2
praice_orange = praice_malini - (praice_malini * 0.4)
praice_banana = praice_malini - (praice_malini * 0.8)

sum_malini = malini_kg * praice_malini
sum_orange = orange_kg * praice_orange
sum_banana = bananas_kg * praice_banana
sum_strobere = strobere_praice * stroberes_kg

all_sum = sum_malini + sum_orange + sum_banana + sum_strobere

print(all_sum)