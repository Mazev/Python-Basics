badget = float(input())
statist = int(input())
dress = float(input())

dekor = badget * 0.1
dress_statist = statist * dress
money_needet = dekor + dress_statist


if statist >= 150:
    diskaunt = dress_statist * 0.10
    money_needet = (dekor + dress_statist) - diskaunt

if money_needet <= badget:
    money_left = badget - money_needet
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
elif money_needet >= badget:
    money_left = money_needet - badget
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')