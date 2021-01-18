days_count = int(input())
hours_cont = int(input())
total_praice = 0
for day in range(1 , days_count + 1 ):
    day_praice = 0
    for hour in range(1, hours_cont +1):
        if day % 2 == 0  and hour % 2 !=0:
            day_praice += 2.50
        elif day % 2 !=0  and hour %2 == 0:
            day_praice += 1.25
        else:
            day_praice += 1
    print(f"Day: {day} – {day_praice:.2f} leva")
    total_praice += day_praice
print(f"Total: {total_praice:.2f} leva")