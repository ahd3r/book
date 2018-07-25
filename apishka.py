import json

with open('bd_of_books_json.txt', 'r') as bd:
    bd_of_books=json.load(bd)

with open('books_json.txt', 'r') as inside:
    books=json.load(inside)

def AddBook():
    input_name = input('Write a name of book: ')
    if input_name in bd_of_books:
        books.append(input_name)
        print('Added.')
    else:
        print('This book not recognized')
    print()

def ListOfBook():
    if books == []:
        print('Nothing')
    else:
        for l in books:
            print(l)
    print()

def ReadBook():
    if books==[]:
        print('You have no any books')
    else:
        already_read=input('Write a book which you have been read: ')
        if already_read in books:
            books[books.index(already_read)]=f'{already_read} — Done'
            print('Done.')
        else:
            print('This book not found!')
    print()

def DeleteBook():
    if books==[]:
        print('You cant delete nothing')
    else:
        input_delete=input('Write a book which you want to delete: ')
        input_delete_done=f'{input_delete} — Done'
        if input_delete in books:
            books.remove(input_delete)
            print('Deleted.')
        elif input_delete_done in books:
            books.remove(input_delete_done)
            print('Deleted.')
        else:
            print('This book not found!')
    print()
