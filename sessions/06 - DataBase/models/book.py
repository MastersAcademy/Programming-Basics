from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    author = Column(String(50), nullable=False)
    description = Column(String(250))
    rating = Column(Integer)

    def __init__(self, title, author, description, rating):
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


    def __repr__(self):
        return f'<id: {self.id}, title: {self.title}, author: {self.author}, description: {self.description}, rating: {self.rating}>'