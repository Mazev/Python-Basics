floors = int(input())
rooms = int(input())

for floor in range(floors , 0 , -1):
    for room in range(rooms):
        if floor == floors:
            print(f'L{floor}{room}', end= ' ')
        elif floor % 2 == 0:
            print(f'А{floor}{room}', end= ' ')
        else:
            print(f'O{floor}{room}', end= ' ')
    print()