start_of_interval_for_first_first_number = int(input())
start_of_interval_for_first_second_number = int(input())
start_of_interval_for_second_first_number = int(input())
start_of_interval_for_second_second_number = int(input())
counter_of_changes = 0
for first_number_first_digit in range(start_of_interval_for_first_first_number, 9):
    if first_number_first_digit % 2 == 0:
        for first_number_second_digit in range(9, start_of_interval_for_first_second_number - 1, -1):
            if first_number_second_digit % 2 != 0:
                for second_number_first_digit in range(start_of_interval_for_second_first_number, 9):
                    if second_number_first_digit % 2 == 0:
                        for second_number_second_digit in range(9, start_of_interval_for_second_second_number - 1, -1):
                            if second_number_second_digit % 2 != 0:
                                if first_number_first_digit == second_number_first_digit and first_number_second_digit == second_number_second_digit:
                                    print("Cannot change the same player.")
                                else:
                                    print(
                                        f"{first_number_first_digit}{first_number_second_digit} - {second_number_first_digit}{second_number_second_digit}")
                                    counter_of_changes += 1
                                    if counter_of_changes == 6:
                                        exit()