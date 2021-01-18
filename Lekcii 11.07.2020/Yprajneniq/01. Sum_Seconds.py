import math

time_firste = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_firste + time_second + time_third

minets = total_time / 60
seconds = total_time % 60

minets = math.floor(minets)

if seconds < 10 :
    print(f'{minets}:0{seconds}')
else:
    print(f'{minets}:{seconds}')



