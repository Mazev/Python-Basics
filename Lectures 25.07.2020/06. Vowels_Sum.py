# text = input()
# total = 0
# for index in range(len(text)):
#     if text[index] == 'a':
#         total += 1
#     elif text[index] == 'e':
#         total += 2
#     elif text[index] == 'i':
#         total += 3
#     elif text[index] == 'o':
#         total += 4
#     elif text[index] == 'u':
#         total += 5
# print(total)

text = input()
total = 0
for i in range(len(text)):
    if text[i] == 'a':
        total += 1
    elif text[i] == 'e':
        total += 2
    elif text[i] == 'i':
        total += 3
    elif text[i] == 'o':
        total += 4
    elif text[i] == 'u':
        total += 5
print(total)