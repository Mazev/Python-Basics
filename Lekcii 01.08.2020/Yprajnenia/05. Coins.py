change_coins = float(input())
coint_count = 0
chaige_in_coins = int(change_coins * 100)
while change_coins > 0:
    if chaige_in_coins >= 200:
        coint_count += 1
        chaige_in_coins -= 200
    elif chaige_in_coins >= 100:
        coint_count += 1
        chaige_in_coins -= 100
    elif chaige_in_coins >= 50:
        coint_count += 1
        chaige_in_coins -= 50
    elif chaige_in_coins >= 20:
        coint_count += 1
        chaige_in_coins -= 20
    elif chaige_in_coins >= 10:
        coint_count += 1
        chaige_in_coins -= 10
    elif chaige_in_coins >= 5:
        coint_count += 1
        chaige_in_coins -= 5
    elif chaige_in_coins >= 2:
        coint_count += 1
        chaige_in_coins -= 2
    elif chaige_in_coins >= 1:
        coint_count += 1
        chaige_in_coins -= 1
        break
print(coint_count)
