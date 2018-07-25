import apishka
import json

'''
Book search
'''

def menu():
	text = '''- `a` to add a new book
- `l` to list a books
- `r` to mark a book as a read
- `d` delete a book
- `q` quite
'''
	user_input=input(text)

	while user_input != 'q':
		if user_input == 'a':
			apishka.AddBook()
		elif user_input == 'l':
			apishka.ListOfBook()
		elif user_input == 'r':
			apishka.ReadBook()
		elif user_input == 'd':
			apishka.DeleteBook()
		else:
			print('Not found')
			print()
		user_input=input(text)

	with open('text_books_json.txt', 'w') as outside:
		json.dump(apishka.books ,outside)


menu()