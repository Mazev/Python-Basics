tempricher = int(input())
denonoshtie = input()

outfit = ''
shoes = ''

if denonoshtie == 'Morning':
    if 10 <= tempricher <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < tempricher <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
if denonoshtie == 'Afternoon':
    if 10 <= tempricher <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < tempricher <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
if denonoshtie == 'Evening':
    if 10 <= tempricher <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < tempricher <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {tempricher} degrees, get your {outfit} and {shoes}.")
