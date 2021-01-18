books = input()
books_conter = 0
while True :
    line = input()
    if line == 'No More Books':
        print("The book you search is not here!")
        print(f"You checked {books_conter} books.")
        break
    if line == books:
        print(f"You checked {books_conter} books and found it.")
        break
    books_conter +=1
