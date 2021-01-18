degrees = int(input())
vreme_ot_denq = input() # "Morning", "Afternoon" или "Evening"
Outfit= ''
Shoes = ''


if 10<= degrees <= 18:
    if vreme_ot_denq == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif vreme_ot_denq == "Afternoon":
        Outfit = 'Shirt'
        Shoes = "Moccasins"
    elif vreme_ot_denq == "Evening":
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
if 18 < degrees <=24:
    if vreme_ot_denq == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif vreme_ot_denq == "Afternoon":
        Outfit = 'T-Shirt'
        Shoes = "Sandals"
    elif vreme_ot_denq == "Evening":
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
if degrees >= 25:
    if vreme_ot_denq == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif vreme_ot_denq == "Afternoon":
        Outfit = 'Swim Suit'
        Shoes = "Sandals"
    elif vreme_ot_denq == "Evening":
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")




