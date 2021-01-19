daljina = float(input())
shirina = float(input())
visochina = float(input())
procent_obem = float(input())

obem = daljina * shirina * visochina
obshti_litri = obem * 0.001
procenta = procent_obem * 0.01
kolko_trqbva = obshti_litri * (1 - procenta)

print(kolko_trqbva)
