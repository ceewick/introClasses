## Abstraction & Encapsulation
## Example = Driving car, taking car to stop. Need to apply break, 
## dont need to know what happens internally
## apply break=abstraction; behind scenes=Encapsulation

## Class <= Library
## Layerts of Abstraction <= Display available books, lend a book, add a book

## Class <= Customer
## Layers of Abstraction <= request book, return book

class Library:
    def __init__ (self, listOfBooks):
        self.availableBooks = listOfBooks
        
    def displayAvailBooks(self):
        print()
        print('Available Books: ')
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print ('you have now borrowd a book')
            self.availableBooks.remove(requestedBook)
        else:
            print('Book not available')
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print('You have returned a book')

class Customer:
    def requestBook(self):
        print('Enter the name of a book you would like to borrow: ')
        self.book = input()
        return self.book
    
    def returnBook(self):
        print('Enter name of book returning')
        self.book = input()
        return self.book

library = Library(['Think & Grow Rich', 
                  'Who Will Cry when you Die?', 
                  'For One More Day'
                  ])
customer = Customer()

while True:
    print('''Enter 1 to display the available books\nEnter 2 to request a book\nEnter 3 to return a book\nEnter 4 to Exit''')
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()