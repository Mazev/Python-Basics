command = input()
total_standart_tikets = 0
total_student_tikets = 0
total_kid_tikets = 0
total_tikets_counter = 0
while command != 'Finish':
    movi_name = command
    tikets_for_sale = int(input())
    sold_tikets = 0
    student_tikets = 0
    standart_tikets = 0
    kid_tikets = 0
    while sold_tikets < tikets_for_sale:
        type_of_tikets = input()
        if type_of_tikets == 'End':
            break
        else:
            total_tikets_counter += 1
            sold_tikets += 1
            if type_of_tikets == 'standard':
                standart_tikets +=1
                total_standart_tikets += 1
            elif type_of_tikets == 'student':
                student_tikets +=1
                total_student_tikets += 1
            elif type_of_tikets == 'kid':
                kid_tikets +=1
                total_kid_tikets += 1
    zapalnena_zala = (student_tikets + standart_tikets + kid_tikets) / tikets_for_sale * 100
    print(f"{movi_name} - {zapalnena_zala}% full.")

percent_of_students_tikets = total_student_tikets / total_tikets_counter * 100
percent_of_standart_tikets = total_standart_tikets / total_tikets_counter * 100
percent_of_kid_tikets = total_kid_tikets / total_tikets_counter * 100
print(f"Total tickets: {total_tikets_counter}")
print(f"{percent_of_students_tikets}% student tickets.")
print(f"{percent_of_standart_tikets}% standard tickets.")
print(f"{percent_of_kid_tikets}% kids tickets.")

