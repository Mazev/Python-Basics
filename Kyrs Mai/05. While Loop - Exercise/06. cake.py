shirina = int(input())
daljina = int(input())

razmer_torta = shirina * daljina


while razmer_torta >0 :
    line = input()
    if line == 'STOP':
        break
    razmer_torta -= int(line)

if razmer_torta < 0:
    print(f"No more cake left! You need {abs(razmer_torta)} pieces more.")
else:
    print(f"{razmer_torta} pieces are left.")
