username = input()
password = input()
data = 0
while data != password:
    data = input()
    if data == password:
        print(f'Welcome {username}!')