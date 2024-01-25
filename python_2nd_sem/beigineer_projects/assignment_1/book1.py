class LibraryBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"Book '{self.title}' by {self.author} borrowed successfully.")
        else:
            print(f"Book '{self.title}' is not available for borrowing.")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Book '{self.title}' by {self.author} returned successfully.")
        else:
            print(f"Book '{self.title}' is already available.")

# Example usage
book1 = LibraryBook("The Catcher in the Rye", "J.D. Salinger")
book1.borrow_book()
book1.return_book()
book1.borrow_book()
