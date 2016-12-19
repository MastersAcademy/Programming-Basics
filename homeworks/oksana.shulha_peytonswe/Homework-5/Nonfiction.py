from Genres import Genres

class Nonfiction(Genres):
    def __init__(self, author, title, year_of_writing, number_of_pages, theme):
        super().__init__(author, title, year_of_writing, number_of_pages)
        self.theme = theme

    def availability(self, reader_age):
        if reader_age <= 18:
            return ("This book is for readers over 18 years!")
        else:
            return ("This book is for all age groups!")
