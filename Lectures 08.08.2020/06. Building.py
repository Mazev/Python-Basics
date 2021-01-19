total_floars = int(input())
total_rooms = int(input())

for floar in range(total_floars , 0 , -1):
    room_tupe = ''
    if floar == total_floars:
        room_tupe = 'L'
    elif floar % 2 == 1:
        room_tupe = 'A'
    else:
        room_tupe = 'O'
    for rooms in range(total_rooms):
        print(f'{room_tupe}{floar}{rooms}', end = ' ')

    print()
