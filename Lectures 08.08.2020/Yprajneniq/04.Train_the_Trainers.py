# средната оценка от представянето на всяка една презентация от даден студент
# а накрая - средния успех от всички тях

judge_counte = int(input())
name_prezentacion = input()
finel_grade = 0
counte_prezentacion = 0

while name_prezentacion != 'Finish':
    grade_sum = 0
    for i in range(judge_counte):
        grade = float(input())
        grade_sum += grade
    avarege_grade = grade_sum / judge_counte
    print(f"{name_prezentacion} - {avarege_grade:.2f}.")

    finel_grade += avarege_grade
    counte_prezentacion += 1
    name_prezentacion = input()
finel_grade /= counte_prezentacion
print(f"Student's final assessment is {finel_grade:.2f}.")
