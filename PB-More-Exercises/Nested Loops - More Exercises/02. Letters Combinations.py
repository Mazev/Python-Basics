bukva_1 = input()
bukva_2 = input()
bukva_3 = input()
counter = 0
for x in range(97, 122 + 1):
    # if x == ord(bukva_3):
    #     continue
    for y in range(97, 122 + 1):
        # if y == ord(bukva_3):
        #     continue
        for z in range(97, 122 + 1 ):
            if z == ord(bukva_3):
                continue
            counter += 1
            print(f'{chr(x)}{chr(y)}{chr(z)} ', end= ' ')

    print(counter)



