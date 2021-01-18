depozit_money = float(input())
time_depozit = int(input())
year_percent = float(input())

money = depozit_money + time_depozit * ((depozit_money * year_percent)/12)

print(money)