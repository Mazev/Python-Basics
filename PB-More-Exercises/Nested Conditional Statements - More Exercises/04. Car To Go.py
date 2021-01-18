budget = float(input())
sezon = input()

klass_kola = ''
vid_kola = ''
praice = 0
if budget <= 100:
    klass_kola = "Economy class"
    if sezon == 'Summer':
        vid_kola = 'Cabrio'
        praice = budget * 0.35
    elif sezon == 'Winter':
        vid_kola = 'Jeep'
        praice = budget * 0.65
elif 100 < budget <= 500:
    klass_kola = 'Compact class'
    if sezon == "Summer":
        vid_kola = 'Cabrio'
        praice = budget * 0.45
    elif sezon == 'Winter':
        vid_kola = 'Jeep'
        praice = budget * 0.80
elif budget > 500:
    klass_kola = 'Luxury class'
    if sezon == 'Summer' or sezon == 'Winter':
        vid_kola = 'Jeep'
        praice = budget * 0.90
print(f'{klass_kola}')
print(f'{vid_kola} - {praice:.2f}')