ekskurzia = float(input())
num_pazel = int(input())
num_kukla = int(input())
num_mecheta = int(input())
num_minioni = int(input())
num_kamioni = int(input())
pazel = 2.60
kukla = 3
meche = 4.10
minioni = 8.20
kamioni = 2
broi_igrachi = num_pazel + num_kukla + num_mecheta + num_minioni + num_kamioni
money = num_pazel * pazel + num_kukla * kukla + num_mecheta * meche + num_minioni * minioni + num_kamioni * kamioni

if broi_igrachi >= 50:
    otstapka = money * 0.25
    naem = (money - otstapka)*0.10
    razhodi = otstapka + naem
    total = money - razhodi
if total > ekskurzia :
    print(f"Yes! {abs(total - ekskurzia):.2f} lv left.")
else:
    print(f"Not enough money! {abs(ekskurzia - total):.2f} lv needed.")