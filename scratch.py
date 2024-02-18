class Library():
    def __init__(self, filename="books.txt"):
        self.filename = open(filename, "a+",encoding="utf-8")

    def __del__(self):
        self.filename.close()

    def list_books(self):
        self.filename.seek(0)
        satirlar=self.filename.read().splitlines()
        for book in satirlar:
            title, author, release_year, page_number = book.split(",")
            print(f"Title: {title}, Author: {author}")


    def add_books(self):
        title = input("Title of the book:")
        author = input("Name of the author:")
        release_year = input("First release year of the book:")
        page_number = input("The number of pages of the book:")
        self.filename.seek(0, 2)
        eklenecek = f"{title},{author},{release_year},{page_number}\n"
        self.filename.write(eklenecek)

    def sil_books(self):
        title = input("Title of the book that you want to remove:")
        self.filename.seek(0)
        kitaps = self.filename.readlines()
        self.filename.seek(0)
        print(kitaps)
        self.filename.truncate()
        for book in kitaps:
            kitap_title = book.strip().split(",")[0]
            if kitap_title.lower() != title.lower():
                self.filename.write(book)


lib = Library()

while True:
    print("""
    *********************************
    Welcome to the Library Management System
                    MENU
    1-)list Books
    2-)Add Book
    3)Remove Book
    If you want to exit, press 'q'.

    *********************************""")
    choose = input("Enter what you do (with respective number):")
    if choose == "1":
        lib.list_books()
    elif choose == "2":
        lib.add_books()
    elif choose == "3":
        lib.sil_books()
    elif choose == "q":
        lib.__del__()
        break
    else:
        print("Wrong command, try again!")