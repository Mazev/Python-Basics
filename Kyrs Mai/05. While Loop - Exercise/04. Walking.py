steps_goal = 10000
steps_counter = 0

while steps_counter < steps_goal:
    line = input()
    if line == 'Going home':
        steps_to_home = int(input())
        steps_counter += steps_to_home
        break

    steps = int(line)
    steps_counter += steps

if steps_goal < steps_counter:
    total = steps_counter - steps_goal
    print('Goal reached! Good job!')
    print(f'{total} steps over the goal!')
else:
    print(f"{steps_goal - steps_counter} more steps to reach goal.")