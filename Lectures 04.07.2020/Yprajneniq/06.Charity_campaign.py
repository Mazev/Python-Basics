day_campaign = int(input())
confectioners = int(input())
cakes = int(input())
gofreti = int(input())
palachinki = int(input())

sum_cakes = 45 * cakes
sum_gofreti = 5.80 * gofreti
sum_palachinki = 3.20 * palachinki

all_for_day = (sum_cakes + sum_gofreti + sum_palachinki) * confectioners
all_money = all_for_day * day_campaign
kraina_suma = all_money - (all_money * 1/8)

print(f"{kraina_suma:.2f}")

