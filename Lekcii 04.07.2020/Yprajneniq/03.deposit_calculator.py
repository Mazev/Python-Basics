#сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_sum = float(input())
duration = int(input())
year_percentage = float(input())



sum = deposit_sum + duration * ((deposit_sum * year_percentage/100)/12)

print(sum)
