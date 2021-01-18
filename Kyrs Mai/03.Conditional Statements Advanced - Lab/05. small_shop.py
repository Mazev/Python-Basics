product = input()
city = input()
quantity = float(input())
praice = 0
if city == 'Sofia':
    if product == 'coffee':
        praice = 0.50
    elif product == 'water':
        praice = 0.80
    elif product == 'beer':
        praice = 1.20
    elif product == 'sweets':
        praice = 1.45
    elif product == 'peanuts':
        praice = 1.60
if city == 'Plovdiv':
    if product == 'coffee':
        praice =0.40
    elif product == 'water':
        praice = 0.70
    elif product == 'beer':
        praice = 1.15
    elif product == 'sweets':
        praice = 1.30
    elif product == 'peanuts':
        praice = 1.50
if city == 'Varna':
    if product == 'coffee':
        praice =0.45
    elif product == 'water':
        praice = 0.70
    elif product == 'beer':
        praice = 1.10
    elif product == 'sweets':
        praice = 1.35
    elif product == 'peanuts':
        praice = 1.55
print(praice * quantity)