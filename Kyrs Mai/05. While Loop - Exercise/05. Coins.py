money = float(input())
resto = money * 100
coints_counter = 0

while True:
    coints_counter += 1
    if resto >= 200:
        resto -= 200
    elif resto >= 100:
        resto -= 100
    elif resto >= 50:
        resto -= 50
    elif resto >= 20:
        resto -= 20
    elif resto >= 10:
        resto -= 10
    elif resto >= 5:
        resto -= 5
    elif resto >= 2:
        resto -= 2
    elif resto >= 1:
        resto -= 1
    if resto < 1:
        break
print(coints_counter)
