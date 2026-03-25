class library:
    def __init__(self):
        self.bookshelf=["rich dad","poor dad ","The exelent"]

    def add_book(self):
        val = input("Enteer the book name")
        self.bookshelf.append(val)  

    def book_issue(self):
        print("The book you want to issue>>",self.bookshelf)
        no = int(input("Enter the  no. of the book you want  from shelf  "))
        issued = self.bookshelf.pop(no - 1)
        print ("your choice.. ",issued)

    def avaliable_book(self):
        print("The avaliable books are .. ",self.bookshelf)

def main():
    win = library()
    while True:
        choice = input(""" select the function 
                       1. To add books
                       2. To issue book
                       3. To see avaliable books
                       4, to exit
                       """)
        if choice =="1":
            win.add_book()
        elif choice =="2":
            win.book_issue()
        elif choice == "3":
            win.avaliable_book()
        elif choice =="4":
            print("code is over ")
            break
        else:
            print("invalid input")
main()                    
