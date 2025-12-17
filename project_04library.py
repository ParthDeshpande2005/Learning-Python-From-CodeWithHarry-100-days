# #%%
# for thking varables as instance
class lib:
    def __init__(self):
        self.no=0
        self.books=[]
#and so on

#%%
#here i have taken variables as class variables
class library:
    def __init__(self,books,no_books):
        self.no_books=no_books
        self.books=books
    
    def info(self):
        print(f"no of books are {self.no_books} which are {self.books}")
    
    def verify(self):
        if(no_books==len(books)):
            print("no of books are correct")
        else:
            print("no of books is incorrect and new no of books is :",len(books))
            self.no_books=len(self.books)
    
    def add(self):
        added=input("enter the names of book to add:")
        new_book=added.split(" ")
        self.books=books+new_book
        self.no_books=len(self.books)
    

no_books=int(input("Enter no of books"))
book=input("enter the names of books:")
books=book.split(" ")
l1=library(books,no_books)


l1.info()
l1.verify()
l1.add()
l1.info()

