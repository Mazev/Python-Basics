money = float(input())
godina = int(input())

money_left = money
ivancho_godini = 18
for broiach_godini in range(1800, godina + 1):
    if broiach_godini % 2 == 0:
        money_left -= 12000
    else:
        money_left -= (12000 + (ivancho_godini * 50))
    ivancho_godini += 1

if money_left >= 0 :
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left." )
else:
    print(f"He will need {abs(money_left):.2f} dollars to survive." )