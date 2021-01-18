broi_hora = int(input())
tochki_plear = int(input())
krav_ilidan = int(input())
tochki = broi_hora * tochki_plear
total = abs(tochki - krav_ilidan)
if total > krav_ilidan:
    print(f"Illidan has been slain! "
          f"You defeated him with {total} points.")
else:
    print(f"You are not prepared! "
          f"You need {total} more points.")