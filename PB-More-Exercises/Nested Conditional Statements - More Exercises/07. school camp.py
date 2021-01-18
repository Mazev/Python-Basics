sezon = input()
vid_grupa = input()
count_schools = int(input())
count_naths = int(input())
money = 0
discount = 0
vid_sport = ''
if sezon == 'Winter':
    if vid_grupa == 'boys':
        vid_sport = 'Judo'
        if count_schools < 10:
            money = count_schools * 9.60 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.50
    elif vid_grupa == 'girls':
        vid_sport = 'Gymnastics'
        if count_schools < 10:
            money = count_schools * 9.60 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 9.60 * count_naths
            discount = money * 0.50
    elif vid_grupa == 'mixed':
        vid_sport = 'Ski'
        if count_schools < 10:
            money = count_schools * 10 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 10 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 10 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 10 * count_naths
            discount = money * 0.50
elif sezon == 'Spring':
    if vid_grupa == 'boys':
        vid_sport = 'Tennis'
        if count_schools < 10:
            money = count_schools * 7.20 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.50
    elif vid_grupa == 'girls':
        vid_sport = 'Athletics'
        if count_schools < 10:
            money = count_schools * 7.20 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 7.20 * count_naths
            discount = money * 0.50
    elif vid_grupa == 'mixed':
        vid_sport = 'Cycling'
        if count_schools < 10:
            money = count_schools * 9.50 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 9.50 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 9.50 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 9.50 * count_naths
            discount = money * 0.50
elif sezon == 'Summer':
    if vid_grupa == 'boys':
        vid_sport = 'Football'
        if count_schools < 10:
            money = count_schools * 15 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 15 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 15 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 15 * count_naths
            discount = money * 0.50
    elif vid_grupa == 'girls':
        vid_sport = 'Volleyball'
        if count_schools < 10:
            money = count_schools * 15 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 15 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 15 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 15 * count_naths
            discount = money * 0.20
    elif vid_grupa == 'mixed':
        vid_sport = 'Swimming'
        if count_schools < 10:
            money = count_schools *  20 * count_naths
        elif 10 <= count_schools < 20:
            money = count_schools * 20 * count_naths
            discount = money * 0.05
        elif 20 <= count_schools < 50:
            money = count_schools * 20 * count_naths
            discount = money * 0.15
        elif count_schools >= 50:
            money = count_schools * 20 * count_naths
            discount = money * 0.50
total = money - discount
print(f'{vid_sport} {total:.2f} lv.')
