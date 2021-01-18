hours = int(input())
minutes = int(input())

minutes = minutes + 15

if minutes > 60:
    hours = hours + 1
    minutes = minutes - 60

if 0 <= minutes <= 9:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')