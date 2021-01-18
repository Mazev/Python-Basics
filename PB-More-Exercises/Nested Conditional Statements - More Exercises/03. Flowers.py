hrizantemi = int(input())
rozi = int(input())
lale = int(input())
sezon = input()
vid_den = input()
cvetq_count = 0
aranjirovka = 2
cvetq_counter = hrizantemi + rozi + lale
praise = 0
if sezon == 'Spring' or sezon == 'Summer':
    praise = hrizantemi * 2 + rozi * 4.10 + lale * 2.50
    if vid_den == 'Y':
        praise += praise * 0.15
        if lale > 7:
            praise -= praise * 0.05
        if cvetq_counter > 20:
            praise -= praise * 0.20
    else:
        if lale > 7:
            praise -= praise * 0.05
        if cvetq_counter > 20:
            praise -= praise * 0.20
elif sezon == 'Autumn' or sezon == 'Winter':
    praise = hrizantemi * 3.75 + rozi * 4.50 + lale * 4.15
    if vid_den == 'Y':
        praise += praise * 0.15
        if 10 <= rozi:
            praise -= praise * 0.10
        if cvetq_counter > 20:
            praise -= praise * 0.20
    else:
        if 10 <= rozi:
            praise -= praise * 0.10
        if cvetq_counter >= 20:
            praise -= praise * 0.20
print(f'{praise + aranjirovka:.2f}')