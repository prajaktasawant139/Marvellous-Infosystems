class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.Name, "by", self.Author + ".", "No of books:", BookStore.NoOfBooks)


    @classmethod
    def GetBookCount(cls):
            print("Total books:", cls.NoOfBooks)


    @staticmethod
    def Info():
        print("BookStore class stores book information.")



Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()


BookStore.GetBookCount()

BookStore.Info()

