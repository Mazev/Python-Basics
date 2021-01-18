molivi = int(input())
cvetni_flumasteri = int(input())
skicnici_resuvane = int(input())
tetradki = int(input())

molivi_praice = 4.75
flumasteri_praice = 1.80
skicnici_praice = 6.50
tetradki_praice = 2.50

praice = molivi * molivi_praice + cvetni_flumasteri * flumasteri_praice + skicnici_resuvane * skicnici_praice + tetradki * tetradki_praice
otstapka = praice - ((praice * 5)/100)

print(f"Your total is {otstapka:.2f}lv")

