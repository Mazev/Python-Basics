pileshko_menu = int(input())
riba_menu = int(input())
vegan_menu = int(input())
pileshko_cena = 10.35
riba_cena = 12.40
vegan_cena = 8.15
transport = 2.50
porachka = pileshko_menu * pileshko_cena + riba_menu * riba_cena + vegan_menu * vegan_cena
desert = (porachka / 100 ) * 20
total = porachka + desert + transport
print(f'Total: {total:.2f}')
