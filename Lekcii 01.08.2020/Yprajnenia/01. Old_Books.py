# book_name = input()
# book_count = 0
# is_book_found = False
# current_books = input()
# while current_books != "Mo More Books":
#     if current_books == book_name:
#         is_book_found = True
#         print(f"You checked {book_count} books and found it.")
#         break
#     book_count += 1
#     current_books = input()
#
#     if not is_book_found:
#         print("The book you search is not here!")
#         print(f'You checked {book_count} books.')
#         break


book_name = input()
book_count = 0
while True:
    current_book = input()
    if current_book == book_name:
        print(f"You checked {book_count} books and found it.")
        break
    if current_book == "No More Books":
        print("The book you search is not here!")
        print(f'You checked {book_count} books.')
        break

    book_count += 1
