month = input()
hours = int(input())
people_in_group = int(input())
time_of_day = input()
hourly_price_per_person = 0
if time_of_day == "day":
    if month == "march" or month == "april" or month == "may":
        hourly_price_per_person = 10.50
    elif month == "june" or month == "july" or month == "august":
        hourly_price_per_person = 12.60
else:
    if month == "march" or month == "april" or month == "may":
        hourly_price_per_person = 8.40
    elif month == "june" or month == "july" or month == "august":
        hourly_price_per_person = 10.20

if people_in_group >= 4:
    hourly_price_per_person *= 0.9

if hours >= 5:
    hourly_price_per_person /= 2

total_price = hourly_price_per_person * people_in_group * hours

print(f"Price per person for one hour: {hourly_price_per_person:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")