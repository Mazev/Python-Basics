total_steps = 0
steps_home = 0
while total_steps < 10000:
    steps = input()
    if steps == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        break
    else:
        total_steps += int(steps)
if total_steps > 10000:
    print('Goal reached! Good job!')
    print(f'{total_steps - 10000} steps over the goal!')
else:
    print(f'{10000 - total_steps} more steps to reach goal.')

