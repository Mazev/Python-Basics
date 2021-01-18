furst_number = int(input())
second_number = int(input())
megec_number = int(input())
combination = False
counter = 0
for h in range(furst_number, second_number + 1):
    for y in range(furst_number, second_number + 1):
        counter += 1
        if h + y == megec_number:
            combination = True
            print(f"Combination N:{counter} ({h} + {y} = {megec_number})")
            break
    if combination:
        break
if not combination:
    print(f'{counter} combinations - neither equals {megec_number}')
