import  math
time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first + time_second + time_third
minets = total_time // 60
seconds = total_time % 60
if seconds < 10:
    print(f'{round(minets)}:0{seconds}')
else:
    print(f'{round(minets)}:{seconds}')