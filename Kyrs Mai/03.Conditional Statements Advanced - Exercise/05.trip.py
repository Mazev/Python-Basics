budget = float(input())
sezons = input()  #"summer” или "winter”
praice = 0
vid_po4ivka = ''
destinaciq = ''
if budget <= 100:
    destinaciq = 'Bulgeria'
    if sezons == 'summer':
        vid_po4ivka = 'Canp'
        praice -= budget * 0.30
    elif sezons == 'winter':
        vid_po4ivka = 'Hotel'
        praice -= budget * 0.70
elif budget <= 1000:
    destinaciq = 'Balkans'
    if sezons == 'summer':
        vid_po4ivka = 'Canp'
        praice -= budget * 0.40
    elif sezons == 'winter':
        vid_po4ivka = 'Hotel'
        praice -= budget * 0.80
elif budget > 1000:
    destinaciq = 'Europe'
    vid_po4ivka = 'Hotel'
    praice -= budget * 0.90

print(f"Somewhere in {destinaciq}")
print(f"{vid_po4ivka} - {abs(praice):.2f}")

