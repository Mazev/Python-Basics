depezit = float(input())
srok_depozit = int(input())
godishna_lihva = float(input())

# money = depezit * godishna_lihva
# mesechna_lihva = money / 12
# total = ((depezit + money) * srok_depozit) * mesechna_lihva

total = depezit + (srok_depozit * (depezit * godishna_lihva) / 12)
print(total)