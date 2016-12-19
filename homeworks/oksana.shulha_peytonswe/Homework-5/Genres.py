class Genres(object):
    def __init__(self, author, title, year_of_writing, number_of_pages):
        self.author = author
        self.title = title
        self.year_of_writing = year_of_writing
        self.number_of_pages = number_of_pages
        
    def info(self):
        return ("author: %s, title: %s, year_of_writing: %i, number_of_pages: %i" % (self.author, self.title, self.year_of_writing, self.number_of_pages))

    def read_book(self):
        return ("This book has been read by you!")

    def current_reading(self):
        return ("This book you read!")

    def future_reading(self):
        return ("This book you want to read!")

    #encapsulation (attribute name is available)
    def _age(self, year_of_writing):
        self.age = 2016 - self.year_of_writing
        print ("This book was written %i years ago." % (self.age))
