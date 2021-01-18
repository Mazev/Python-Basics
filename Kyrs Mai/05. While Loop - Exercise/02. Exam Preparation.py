bad_grades = int(input())
bad_grades_count = 0
avarege_score = 0
test_count = 0
last_name_test = ''

while True :
    name_test = input()
    if name_test == 'Enough':
        print(f"Average score: {avarege_score / test_count:.2f}")
        print(f"Number of problems: {test_count}")
        print(f"Last problem: {last_name_test}")
        break
    last_name_test = name_test
    score = int(input())
    test_count += 1
    avarege_score += score

    if score <= 4:
        bad_grades_count += 1
    if bad_grades_count == bad_grades:
        print(f"You need a break, {bad_grades_count} poor grades.")
        break

