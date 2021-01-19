import math

rekord = float(input())
raztoqnie = float(input())
time_sekonds = float(input())

time_needed = time_sekonds * raztoqnie
delei = math.floor(raztoqnie / 15) * 12.5
total_time = time_needed + delei

if total_time < rekord:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {total_time - rekord:.2f} seconds slower.')