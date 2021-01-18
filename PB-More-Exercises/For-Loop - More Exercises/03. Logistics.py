tovari = int(input())
tonaj = 0
mikrobus = 0
kamion = 0
vlak = 0
for i in range(tovari):
    tonaj = int(input())
    if tonaj <= 3:
        mikrobus += tonaj
    elif 4 <= tonaj <= 11:
        kamion += tonaj
    elif tonaj >= 12:
        vlak += tonaj
tovar = mikrobus + kamion + vlak
sredno_za_ton = (mikrobus * 200 + kamion * 175 + vlak * 120) / tovar
print(f'{sredno_za_ton:.2f}')
print(f'{(mikrobus / tovar)* 100:.2f}%')
print(f'{(kamion / tovar) * 100:.2f}%')
print(f'{(vlak / tovar) * 100:.2f}%')
