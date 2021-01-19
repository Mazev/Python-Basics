shirina = int(input())
daljina = int(input())
visochina = int(input())
obem_staq = shirina * daljina * visochina
space_need = 0
line = input()
while line != 'Done':
    current_box_space = int(line)
    space_need += current_box_space
    if space_need > obem_staq:
        break
    line= input()
if space_need > obem_staq:
    print(f'No more free space! You need {space_need - obem_staq} Cubic meters more.')
else:
    print(f'{obem_staq - space_need} Cubic meters left.')
