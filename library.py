class Book:
    def __init__(self, id, book_name, quantity) -> None:
        self.id = id
        self.book_name = book_name
        self.quantity = quantity

class User:
    def __init__(self, id, name, password) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.borrowed_book = []
        self.returned_book = []

class Library:
    def __init__(self, name) -> None:
        self.name = name
        self.users = []
        self.books = []

    def addBooks(self, id, name, quantity):
        book = Book(id, name, quantity)
        self.books.append(book)
        print(f"{name} added successfully ! \n")

    def removeBooks(self, book_id):
        for book in self.books:
            if book.id == book_id:
                book_name = book.book_name
                index = self.books.index(book)
                self.books.pop(index)
                print(f"{book_name} removed successfully !\n")

    def addUser(self, id, name, password):
        user = User(id,name,password)
        self.users.append(user)
    def borrowBook(self, token, user):
        for book in self.books:
            if book.book_name == token:
                if book in user.borrowed_book:
                    print("So you borrowed the book.....")
                    if book in user.returned_book:
                        print("And You return the book..")
                        if book.quantity > 0:
                            print("Book are available")
                            user.borrowed_book.append(book)
                            book.quantity -= 1
                            print(f"Congratulation ! you successfully borrowed {token}\n")
                            return
                        else:
                            print("No copy Available")
                            return
                    else:
                        print("but You did't return the book")
                        return
                else:
                    if book.quantity > 0:
                            user.borrowed_book.append(book)
                            book.quantity -= 1
                            print(f"Congratulation ! you successfully borrowed {token}\n")
                            return
                    else:
                            print("No copy Available")
                            return
        print(f"There is no book in library named {token}")

    def returnBook(self, token, user):
        for book in self.books:
            if book.book_name == token:
                if book in user.borrowed_book:
                    user.returned_book.append(book)
                    book.quantity +=1
                    print("Thank you to return the book")
                    return
                else:
                    print("Your did not borrow the book")
                    return
        print("This book is not of this library")


                    




bsk = Library("Bisho shahitto kendro")
admin = bsk.addUser(1, "admin", "admin")
meherab = bsk.addUser(17, "meherab", "123")
cpBook = bsk.addBooks(11, "cp book", 5)

currentUser = None
while(True):
    if currentUser == None:
        print("Not Lonig")
        option = input("login or register (L/R): ")
        if option == "L":
            id = int(input("Enter Id: "))
            password = input("Enter Password: ")
            print()
            match = False
            for user in bsk.users:
                if user.id == id and user.password == password:
                    currentUser = user
                    match = True
                    break
            if match == False:
                print("No user found")
        elif option == "R":
            id = int(input("Enter Id: "))
            name = input("Enter your Name: ")
            password = input("Enter password: ") 
            user_exist = False
            for user in bsk.users:
               if user.id == id:
                   user_exist = True
                   break
            if user_exist == True:
                print("User already Exists\n")
            else:
                user = bsk.addUser(id,name,password)
                currentUser = user
    else:
        print(f"Wellcome {currentUser.name}\n")
        if currentUser.name =="admin":
            print("options")
            print("1. Add book")
            print("2. Add user")
            print("3. Remove books")
            print("4. See all book list")
            print("5. Logout\n")
            op = input("Enter option: ")
            if op == '1':
                id = int(input("Enter book id: "))
                book_name = input("Enter book name: ")
                quantity = int(input("Enter Number of books: "))
                bsk.addBooks(id,book_name,quantity)
            elif op =='2':
                print("woking on this method\n")
            elif op =='3':
                id  = int(input("Enter Book id: "))
                bsk.removeBooks(id)
            elif op =='4':
                for book in bsk.books:
                    print(f"{book.id}\t{book.book_name}\t{book.quantity}")
                print()
            elif op =='5':
                currentUser = None
        else:
            print("options")
            print("1. Borrow Book")
            print("2. Return Book")
            print("3. See Borrowed Book")
            print("4. See My history")
            print("5. Logout\n")

            op = input("Enter option: ")
            if op =='1':
                name = input("Enter book Name: ")
                bsk.borrowBook(name,currentUser)
            elif op == '2':
                name = input("Enter book name: ")
                bsk.returnBook(name,currentUser)
            elif op == '3':
                print("id\tbook_name")
                for book in currentUser.borrowed_book:
                    print(f"{book.id}\t{book.book_name}")
                print()
            elif op == '4':
                print("id\tbook_name")
                for book in currentUser.returned_book:
                    print(f"{book.id}\t{book.book_name}")
                print()
            elif op =='5':
                currentUser = None