# Problem Statement:
# You are given a list of books and their corresponding authors. 
# Create a dictionary where the keys are the book titles and the values are their 

# Then, find and print the author of a specific book, entered by the user.
# If found show the author of the book searched by the user else show not 
# available in the dictionary.
# Given data
books = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5']
authors = ['Author1', 'Author2', 'Author3', 'Author4', 'Author5']
book_dict = {}
for i in range(len(books)):
    book_dict[books[i]] = authors[i]
print(book_dict)
# Asking the user for a book to search
search_book = input("Enter the name of the book you want to search for: ")
# Checking if the book is in the dictionary
if search_book in book_dict:
    author_of_specific_book = book_dict[search_book]
    print(f"The author of {search_book} is: {author_of_specific_book}")
else:
    print(f"The book '{search_book}' is not found in the dictionary.")