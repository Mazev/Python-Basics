degreas = float(input())
if 26.0 <= degreas <= 35.00 :
    print('Hot')
elif 20.1 <= degreas <= 25.9:
    print('Warm')
elif 15.00 <= degreas <= 20.00:
    print('Mild')
elif 12.00 <= degreas <= 14.9:
    print('Cool')
elif 5.00 <= degreas <= 11.9:
    print('Cold')
else:
    print('unknown')
