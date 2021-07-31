#STUDENT LIBRARY


class library:
        def __init__(self,listofbooks):
            self.books=listofbooks
            print("The books are : ")



        def availableBooks(self):
            for book in self.books:
                print("  $" + book)


        def borrowBook(self,bookname):
            if bookname in self.books:

                print(f"you have issued {bookname} please return before issued date over")
                self.books.remove(bookname)
                return True


            else:
                print("There is no book availabe now")
                return False

        def returnBook(self,bookname):
            self.books.append(bookname)
            print(f"thanls for returning {bookname} book")


            




class student:
        def requestBook(self):
            self.book=input("enter the name of the book : ")
            return self.book

        def returnBook(self):
            self.book=input("enter the name of the book : ")
            return self.book

st=student()





if __name__  == "__main__":
        hackerslibrary=library(["foot printing","python","DSA","burpsuite"])
        # hackerslibrary.availableBooks()
        while(True):
            firstmsg='''     ========WELCOME TO HACKERS CLUB========
            1. ENTER 1 FOR LIST THE BOOKS
            2. ENTER 2 FOR BORROW A BOOK
            3. ENTER 3 FOR RETURN THE BOOK
            4. ENTER 4 FOR EXIT'''
            print(firstmsg)
            try:
                a=int(input("enter the choice : "))
                

                

                

                if a==1:
                    hackerslibrary.availableBooks()

                elif a==2:
                    hackerslibrary.borrowBook(st.requestBook())

                elif a==3:
                    hackerslibrary.returnBook(st.returnBook())

                elif a==4:
                    print("thanks for using our library")
                    exit()

                else:
                    print("invalid choice")
            except Exception as e:
                print("enter only number:")

