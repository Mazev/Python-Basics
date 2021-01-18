chas = int(input())
day = input()
if day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday' or 'Friday' or 'Saturday':
    if 10 <= chas < 18:
        print('open')
    elif 10 < chas >= 18:
        print('closed')
elif day == 'Sunday':
    print('closed')


# 10 >= chas < 18: