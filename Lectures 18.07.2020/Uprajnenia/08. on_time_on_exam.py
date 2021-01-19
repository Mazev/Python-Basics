hour_of_exame = int(input())
minets_of_exame = int(input())
hour_of_arrive = int(input())
minets_of_arrive = int(input())

total_minets_of_exame = hour_of_exame * 60 + minets_of_exame
total_minets_of_arrive = hour_of_arrive * 60 + minets_of_arrive
difference = total_minets_of_arrive - total_minets_of_exame
state = ''

if difference < -30:
    state = 'Early'
elif -30 <= difference <= 0:
    state = 'On time'
else:
    state = 'Late'

result = ''
if difference != 0:
    hour = abs(difference) // 60
    minutes = abs(difference) % 60
    if hour > 0:
        if difference < 0:
            result = f'{hour}:{minutes:02d} hours before the start'
        else:
            result = f'{hour}:{minutes:02d} hours after the start'
    else:
        if difference < 0:
            result = f'{minutes} minutes before the start'
        else:
            result = f'{minutes} minutes after the start'
print(f'{state}')

if difference !=0:
    print(f'{result}')


