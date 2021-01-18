num = int(input())
score = 0
if num <= 100:
    score = 5
elif num > 1000:
    score = num * 0.1
else:
    score = num * 0.20

if num % 2 == 0:
    score += 1
elif num % 10 == 5:
    score += 2
print(score)
print(score + num)