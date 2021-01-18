budget = float(input())
sezon = input()

money_needet = 0
destinacia = ''
if budget <= 100:
    destinacia = 'Bulgaria'
    if sezon == 'summer':
        money_needet = budget * 0.30
        vid_pochivka = 'Camp'
    else:
        money_needet = budget * 0.70
        vid_pochivka = 'Hotel'
elif 100 <= budget <= 1000:
    destinacia = 'Balkans'
    if sezon == 'summer':
        money_needet = budget * 0.40
        vid_pochivka = 'Camp'
    else:
        money_needet = budget * 0.80
        vid_pochivka = 'Hotel'
else :
    destinacia = 'Europe'
    money_needet = budget * 0.90
    vid_pochivka = 'Hotel'
print(f"Somewhere in {destinacia}")
print(f"{vid_pochivka} - {money_needet:.2f}")

