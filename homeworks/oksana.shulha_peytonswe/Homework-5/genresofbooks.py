class Genres_of_books(object):
    def __init__(self, author, title, year_of_writing, number_of_pages):
        self.author = author
        self.title = title
        self.year_of_writing = year_of_writing
        self.number_of_pages = number_of_pages
        

    def info(self):
        print ("author: %s, title: %s, year_of_writing: %i, number_of_pages: %i" % (self.author, self.title, self.year_of_writing, self.number_of_pages))

    def read_book(self):
        print ("This book has been read by you!")

    def current_reading(self):
        print ("This book you read!")

    def future_reading(self):
        print ("This book you want to read!")

#encapsulation (attribute name is available)
    def _howManyYearsThisBook(self, year_of_writing):
        self.age = 2016 - self.year_of_writing
        print ("This book was written %i years ago." % (self.age))
        
#inheritance classes
class Fiction(Genres_of_books):
    def __init__(self, author, title, year_of_writing, number_of_pages, form, kind):
        super().__init__(author, title, year_of_writing, number_of_pages)
        self.form = form
        self.kind = kind


class Non_fiction(Genres_of_books):
    def __init__(self, author, title, year_of_writing, number_of_pages, theme):
        super().__init__(author, title, year_of_writing, number_of_pages)
        self.theme = theme 

        

book1 = Fiction("George Orwell", "1984", 1948, 267, "novel", "dystopian")
book1.info()
book1.read_book()
book1._howManyYearsThisBook(1948)

book2 = Fiction("Aldous Huxley", "Brave New World", 1931, 311,  "novel", "dystopian")
book2.info()
book2.current_reading()

book3 = Non_fiction("Suetonius", "The Lives of the Caesars", 121, 363, "historical biography")
book3.info()
book3.future_reading()
