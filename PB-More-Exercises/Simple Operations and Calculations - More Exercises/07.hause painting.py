x = float(input())
y = float(input())
h = float(input())

prozorci = (1.5 * 1.5) * 2
steni_s_prozorci = (x * y) * 2 - prozorci
vrata = 1.20 * 2
predni_steni = (x * x) * 2 - vrata
pokriv = (x * y) * 2
strani_porkiv = (x * h /2 ) * 2

zbor_steni = steni_s_prozorci + predni_steni
zbor_pokriv = pokriv + strani_porkiv

zelena_boq = zbor_steni / 3.4
chervena_boq = zbor_pokriv / 4.3
print(f'{zelena_boq:.2f}')
print(f'{chervena_boq:.2f}')