from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Factory
from models.book import Book

faker = Factory.create()
Base = declarative_base()

engine = create_engine('sqlite:///06-databases.sqlite')

Base.metadata.create_all(engine)

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_book = Book(title=faker.sentence(), author=faker.name(), description=' '.join(faker.sentences(5)))
