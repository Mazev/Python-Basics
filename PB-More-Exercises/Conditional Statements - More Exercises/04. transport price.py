n_kilometers = int(input())
text = input()

if n_kilometers < 20 and text == 'day':
    print(f'{n_kilometers * 0.79 + 0.70:.2f}')
elif n_kilometers < 20 and text == 'night':
    print(f'{n_kilometers * 0.90 + 0.70:.2f}')

if 20 <= n_kilometers < 100 : 
    print(f'{n_kilometers * 0.09:.2f}')

if n_kilometers >= 100:
    print(f'{n_kilometers * 0.06:.2f}')