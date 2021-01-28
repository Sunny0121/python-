class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. \n !!!!!!-->Please wait until the book is available<--!!!!!")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it.\n Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book
         

if __name__ == "__main__":
    sunnyLibrary = Library(["physics", "the chemist", "C++", "Notes of life","marigold", "Ass pass", "ganit ka jaadu"])
    student = Student()
    # sunnyLibrary.displayAvailableBooks()
    while(True):
        try:
            welMsg = '''\n ======>>>{ Welcome to SUNNY Library }<<<======
            Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the Library
            '''
            print(welMsg)
            a = int(input("Enter your choice: "))
            if a == 1:
                sunnyLibrary.displayAvailableBooks()
            elif a == 2:
                sunnyLibrary.borrowBook(student.requestBook())
            elif a == 3:
                sunnyLibrary.returnBook(student.returnBook())
            elif a == 4:
                print("Thanks for choosing SUNNY Library. Have a great day ahead!")
                exit()
            else:
                print("Invalid Choice!")
        except ValueError as e:
            print(f"You entered {e} your choice must be an integer between 1 - 4 either you can't take any action library")


        
