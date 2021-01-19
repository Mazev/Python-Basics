shirochina = int(input())
visochina = int(input())
torta = shirochina * visochina
while torta > 0:
    line = input()
    if line == 'STOP':
        break
    else:
        parcheta = int(line)
        torta -= parcheta
if torta > 0:
    print(f'{torta} pieces are left.')
else:
    print(f'No more cake left! You need {abs(torta)} pieces more.')
