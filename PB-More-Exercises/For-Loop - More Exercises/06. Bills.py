broi_meseci = int(input())
tok = 0
voda = 20
internet = 15
drugi_smetki = 0
for i in range(broi_meseci):
    tok_mesec = float(input())
    tok += tok_mesec
    razhodi = (tok_mesec + voda + internet) * 0.20
    drugi_smetki += (tok_mesec + voda + internet + razhodi)

total_voda = voda * broi_meseci
total_internet = internet * broi_meseci

print(f"Electricity: {tok:.2f} lv")
print(f"Water: {total_voda:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {drugi_smetki:.2f} lv")
print(f"Average: {(tok + total_voda + total_internet + drugi_smetki)/ broi_meseci:.2f} lv")
