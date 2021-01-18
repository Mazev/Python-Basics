days = int(input())
room = input()
ocenka = input()

niths = days -1

room_for_one_person = 18
apartment = 25
president_apartment = 35

praice_for_days = 0
diskaunt = 0
if niths < 10:
    if room == 'room for one person':
        praice_for_days = room_for_one_person * niths
    elif room == 'apartment':
        praice_for_days = apartment * niths
        diskaunt = praice_for_days * 0.30
    elif room == 'president apartment':
        praice_for_days = president_apartment * niths
        diskaunt = praice_for_days * 0.10
elif 10 <= niths <= 15:
    if room == 'room for one person':
        praice_for_days = room_for_one_person * niths
    elif room == 'apartment':
        praice_for_days = apartment * niths
        diskaunt = praice_for_days * 0.35
    elif room == 'president apartment':
        praice_for_days = president_apartment * niths
        diskaunt = praice_for_days * 0.15
elif niths > 15:
    if room == 'room for one person':
        praice_for_days = room_for_one_person * niths
    elif room == 'apartment':
        praice_for_days = apartment * niths
        diskaunt = praice_for_days * 0.50
    elif room == 'president apartment':
        praice_for_days = president_apartment * niths
        diskaunt = praice_for_days * 0.20
cena_prestoi = praice_for_days - diskaunt
cena_ocenka = 0
if ocenka == 'positive':
    cena_ocenka = cena_prestoi * 0.25
    print(f'{cena_prestoi + cena_ocenka:.2f}')
elif ocenka == 'negative':
    cena_ocenka = cena_prestoi * 0.10
    print(f'{cena_prestoi - cena_ocenka:.2f}')
