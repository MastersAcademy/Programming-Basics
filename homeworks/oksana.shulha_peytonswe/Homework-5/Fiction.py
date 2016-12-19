from Genres import Genres

#inheritance classes
class Fiction(Genres):
    def __init__(self, author, title, year_of_writing, number_of_pages, form, kind):
        super().__init__(author, title, year_of_writing, number_of_pages)
        self.form = form
        self.kind = kind

    def rating(self, likes):
        if likes > 1000:
            return ("This book 5 stars")
        elif likes in range(800,1000):
            return ("This book 4 stars")
        elif likes in range(600,799):
            return ("This book 3 stars")
        elif likes in range(400,599):
            return ("This book 2 stars")
        elif likes in range(200,399):
            return ("This book 1 star")
        else:
            return ("This book 0 stars")
