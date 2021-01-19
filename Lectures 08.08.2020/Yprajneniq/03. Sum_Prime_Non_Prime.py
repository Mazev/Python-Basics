command = input()
sum_prime_num = 0
sum_non_prime_num = 0
while command != 'stop':
    number = int(command)
    demmon_count = 0
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    for i in range(2, number):
        if number % i == 0:
            demmon_count += 1
    if demmon_count == 0:
        sum_prime_num += number
    elif demmon_count > 0:
        sum_non_prime_num += number
    command = input()

print(f"Sum of all prime numbers is: {sum_prime_num}")
print(f"Sum of all non prime numbers is: {sum_non_prime_num}")