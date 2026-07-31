#Library program that allows for storing and adding of new books and patrons
#Use 3 classes 
#define book class --> title, author, is_borrowed  ; addbook(), returnbook(), borrowbook(), checkavail()
#def Patron class --> Name, Id, etc ; booksborrowed() , booksreturned()
#Define class Library --> Displays books (avail / un avail) and patrons
#Store info in dict? or 2D Arrays?


#Final Version

#NOTE to self, if possible , for every major variable / declarations, use lowercase words / letters to make calling easier



class Book:
    
    def __init__(self,title,author,is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrowbook(self): 
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def returnbook(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False

class Patron:
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.borrowedbooks = []

    def addbook(self,book):
        self.borrowedbooks.append(book)

    def removebook(self,book):
        if book in self.borrowedbooks:
            self.borrowedbooks.remove(book)

class Library: 
    def __init__(self): #We use dictionaries here for O(1) lookup time
        self.books = {}
        self.patrons = {}

    def add_book(self,title,author):
        new_book = Book(title,author) 
        self.books[title.lower()] = new_book #Or , you can also do , self.books[title.lower()] = Book(title,author)
        print(f"{title} by {author} has been added to the Library")

    def register_user(self,name,id):
        self.patrons[name.lower()] = Patron(name,id)
        print(f"{name} has been added to the user list")

    def display_books(self):
        if not self.books:
            print("Library is empty")
            return
        
        for book in self.books.values():
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} by {book.author} ; {status}")

    def display_patrons(self):
        if not self.patrons:
            print("No users in database")
            return
        
        for patron in self.patrons.values():   #Here we can invoke the .values() as in the above registration of new patrons, we set [key] = Patrons(name,id) . Therefore, the values of the keys will have all the necessary information incl name and id
            borrowed_books = [b.title for b in patron.borrowedbooks]
            borrowed_str = ", ".join(borrowed_books) if borrowed_books else "None"
            print(f"User: {patron.name} Id: {patron.id} || Borrowed Books : {borrowed_str}")


    def borrow_book(self,title,patronname): #1.Check for patron 2.Check for book 3.Check for availability 4.If yes borrow , else dont
        patron = self.patrons.get(patronname.lower())
        if not patron:
            print(f"{patronname} does not exist in the user list")
            return
        
        book = self.books.get(title.lower())
        if not book:
            print(f"{book} does not exist in this library")
            return

        #Borrow

        if book.borrowbook():
            patron.addbook(book)
            print(f"{book.title} has been checked out by {patronname}")
        else:
            print(f"{book.title} is unavailable")
            
    def return_book(self,title,patronname):
        patron = self.patrons.get(patronname.lower())
        if not patron:
            print(f"{Patron} does not exist in the user list")
            return
        
        book = self.books.get(title.lower())
        if not book:
            print(f"{book} does not exist in this library")
            return

        #return

        if book.returnbook():
            patron.removebook(book)
            print(f"{book.title} has been returned by {patronname}")
        else:
            print(f"{book.title} has already been returned")

#MAIN

my_library = Library()

is_running = True

while (is_running):

    print()
    print("-----------LIBRARY-----------")
    print("1.Display Books\n2.Display Patrons\n3.Add Book\n4.Borrow Book\n5.Return Book\n6.Register New User\n7.Exit")
    try:
        op = int(input(":"))
    except ValueError:
        print("Please Enter a valid integer value between 1 - 7")
        continue

    if op == 1:
        my_library.display_books()

    elif op == 2:
        my_library.display_patrons()

    elif op == 3:
        Btitle = input("Enter title of book: ")
        BAuthor = input("Enter its Author: ")
        my_library.add_book(Btitle,BAuthor)

    elif op == 4:
        Btitle = input("Enter title of book you wish to borrow: ")
        Borrower = input("Enter name of the user borrowing book: ")
        my_library.borrow_book(Btitle,Borrower)

    elif op == 5:
        Btitle = input("Enter the title you are returning: ")
        Borrower = input("Enter name of the user borrowing book: ")
        my_library.return_book(Btitle,Borrower)

    elif op == 6:
        uname = input("Enter name: ")
        uid = input("Enter unique ID: ")
        my_library.register_user(uname,uid)

    elif op == 7:
        print("Exiting...")
        is_running = False



#------------------------------------------

#Following is a documentation of the iterations this program has undergone

#-------------------------------------------


#First Ver.

'''books=[]
patrons = {}

class Book():
    
    def __init__(self,Bookname,Author,is_available = True):
        self.Bookname = Bookname
        self.Author = Author
        self.is_available = is_available
    
    def entry(self):
        entrylist = [self.Bookname,self.Author,"Available" if self.is_available else "Not Available"]
        books.append(entrylist)'''

         
''' def borrowbook(self):
        if (self.is_available) != False and (self.Bookname) in books:
            print(f"{self.Title} has been checked out")
            self.is_available = False
        elif (self.is_available) == False:
            print("Book is unavaiable")
        else:
            print("Book is not in stock")
            
    def returnbook(self):
        if (self.is_available) is False:
            print(f"{self.Bookname} has been returned!")
            self.is_available = True
        else:
            print(f"{self.Bookname} is already in stock")'''
        

'''class Patrons():
    
    def __init__(self,Name,ID):
        self.Name = Name
        self.ID = ID
        
    def register(self):
        patrons[self.Name] = self.ID

class Library():
    
    def displaybooks():
        print(f"Books In Library:\n{books}")
    
    def displaypatrons():
        print(f"Patrons:\n{patrons}")
    
    
#User Inputs

is_running = True

while (is_running):
    
    print()
    print("-----------LIBRARY-----------")
    print("Welcome to the Library! What would you like to do:")
    print("1.Add Book\n2.Borrow Book\n3.Return Book\n4.Register Patron\n5.Display Books\n6.Display Patrons\n7.Exit")
    
    try:
        op = int(input(":"))
    except ValueError:
        print("Please enter an option within (1-6)")
        print()
    
    if op == 1:
        Bname = input("Enter Title of the Book: ")
        Ath = input("Enter Author: ")
        
        Bookentry = Book(Bname,Ath)
        
        Bookentry.entry()
        
    elif op == 2:
        SearchName = input("Enter title of book you want to borrow: ")
        for i in books:
            for j in i[0]:
                if j != SearchName:
                    continue
                else:
                    print("{SearchName} has been issued by you")
                    break
            break
        
    
    elif op == 3:
            SearchName = input("Enter title of book you want to borrow: ")
            for i in books:
                for j in i:
                    if j == SearchName:
                        print(f"{SearchName} has been returned by YOU")
                    else:
                        print("Said book does not exist")
                        
    elif op == 4:
        Patname = input("Enter Patron's Name")
        PatID = input("Enter Patron's ID")
        
        Patentry = Patrons(Patname,PatID)
        Patentry.register()
        
    elif op == 5:
        
        Library.displaybooks()
        
        
    elif op == 6:
        
        Library.displaypatrons()
        
    elif op == 7:
        
        is_running = False
        break
    
    else:
        
        print("Please enter a valid operation")'''
            




#Refined

'''class Book():

    def __init__(self,title,author,is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrowbook(self):
        if self.is_available:
            self.is_available = False
            return True
        return False


    def returnbook(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False

class Patron():
    
    def __init__(self,name,id):
        self.name = name
        self.id = id


class library():
    
    def __init__(self):
        self.books = []
        self.patrons = {}

    def add_books(self,title,author):
        new_book = Book(title,author)
        self.books.append(new_book)
        print(f"{title} has been added to the library!")

    def register_patrons(self,PatName, PatId):
        self.patrons[PatName] = [PatId]
        print(f"User <{PatName} has been registered!")

    def borrow_book(self,title):
        if not self.books:
            print("No Books Available")
        else:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if book.borrowbook():
                        print(f"{book.title} has been checked out by you!")
                    else:
                        print(f"{book.title} is not available")
                    return
                
            print(f"{title} is not in stock")
                
    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.returnbook():
                    print(f"{title} has been returned! Thank you!")
                else:
                    print(f"{title} was never borrowed")
                return
        print(f"{title} does not exist in the Library")

    def display_books(self):
        if not self.books:
            print("No Books are currently available")
        else:
            for book in self.books:
                status = "Available" if book.is_available else "Not Available"
                print("Library Books: ")
                print(f"{book.title} by {book.author}; [{book.is_available}]")


    def display_patrons(self):
        if not self.patrons:
            print("No user data")
        else:
            for username, userid in self.patrons.items():
                print(f"- {username} (ID: {userid})")


#Main

my_library = library()
is_running = True

while is_running:

    print("-----------LIBRARY-----------")
    print("Welcome to the Library! What would you like to do:")
    print("1.Add Book\n2.Borrow Book\n3.Return Book\n4.Register Patron\n5.Display Books\n6.Display Patrons\n7.Exit")
    
    try:
        op = int(input(":"))
    except ValueError:
        print("Please enter an option within (1-7)")
        print()

    if op == 1:
        Bname = input("Enter Book Name: ")
        BAuthor = input("Enter Book's Author: ")
        my_library.add_books(Bname,BAuthor)

    elif op == 2:
        Btitle = input("Enter title of book you wish to borrow: ")
        my_library.borrow_book(Btitle)

    elif op == 3:
        Btitle = input("Enter title of book you wish to return: ")
        my_library.return_book(Btitle)

    elif op == 4:
        Pname = input("Enter Patron's name: ")
        PId = input("Enter Patron's ID: ")
        my_library.register_patrons(Pname,PId)

    elif op == 5:
        my_library.display_books()

    elif op == 6:
        my_library.display_patrons()

    elif op == 7:
        print("Thank you for visiting!")
        is_running = False
    else:
        print("Please enter a valid option (1-7)")'''


#Refined v2

'''class Book:
    
    def __init__(self,title,author,is_available = True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def borrowbook(self): #Here, we set the condition for borrowing a book, i.e, if the book is available , the users / patrons can borrow.If its not available, then they CANT borrow it
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def returnbook(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False

class Patron:

    #What if i make a library that holds the books borrowed by a person?
    #Or do i just tally up the number of times a person borrows books?
    
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def booksborrowed(self):
        pass

    def booksreturned(self):
        pass

class Library: #Main class where all the operations will happen
    
    def __init__(self):
        self.books = []
        self.patrons = {}

    def add_book(self,title,author):
        new_book = Book(title,author)
        self.books.append(new_book)
        print(f"{title} by {author} has been added to the Library")

    def register_user(self,name,id):
        self.patrons[name] = id
        print(f"{name} has been added to the user list")

    def display_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                status = "Available" if book.is_available else "Not Available"
                print(f"{book.title} by {book.author} ; {status}")

    def display_patrons(self):
        if not self.patrons:
            print("No users in database")
        else:
            for username,userid in self.patrons.items():
                print(f"{username} : {userid}")

    def borrow_book(self,title):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if book.borrowbook():
                        print(f"{title} has been issued to you!")
                    else:
                        print(f"{title} is currently unavailable")
                    return
            print(f"{title} does not exist")

    def return_book(self,title):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books:
                if book.title.lower() == title.lower():
                    if not book.returnbook():
                        print(f"{title} has been returned")
                    else:
                        print(f"{title} has already been returned")
                    return
            print(f"{title} does not exist")

    def search_book(self):
        pass

    def search_patron(self):
        pass

#MAIN

my_library = Library()

is_running = True

while (is_running):

    print()
    print("-----------LIBRARY-----------")
    print("1.Display Books\n2.Display Patrons\n3.Add Book\n4.Borrow Book\n5.Return Book\n6.Register New User\n7.Exit")
    try:
        op = int(input(":"))
    except ValueError:
        print("Please Enter a valid integer value between 1 - 7")

    if op == 1:
        my_library.display_books()

    elif op == 2:
        my_library.display_patrons()

    elif op == 3:
        Btitle = input("Enter title of book: ")
        BAuthor = input("Enter its Author: ")
        my_library.add_book(Btitle,BAuthor)

    elif op == 4:
        Btitle = input("Enter title of book you wish to borrow: ")
        my_library.borrow_book(Btitle)

    elif op == 5:
        Btitle = input("Enter the title you are returning: ")
        my_library.return_book(Btitle)

    elif op == 6:
        uname = input("Enter name: ")
        uid = input("Enter unique ID: ")
        my_library.register_user(uname,uid)

    elif op == 7:
        print("Exiting...")
        is_running = False'''
