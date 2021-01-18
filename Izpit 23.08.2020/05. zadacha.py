current_meters = 5364
target_meters = 8848
days = 1
command = input()
while command != "END":
    daily_meters = int(input())
    if command == "Yes":
        days += 1
        if days > 5:
            break
    current_meters += daily_meters
    if current_meters >= target_meters:
        break
    command = input()
if current_meters >= target_meters:
    print(f"Goal reached for {days} days!")
else:
    print("Failed!")
    print(f"{current_meters}")