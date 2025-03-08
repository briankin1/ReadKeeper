
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Relationship with books (One-to-many)
    books = relationship('Book', back_populates='author')
    
    def __repr__(self):
        return f"<Author(name={self.name})>"

class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    # Many-to-many relationship with books
    books = relationship('Book', secondary='book_genres')
    
    def __repr__(self):
        return f"<Genre(name={self.name})>"

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    
    # Relationship with author (Many-to-one)
    author = relationship('Author', back_populates='books')
    
    # Many-to-many relationship with genres
    genres = relationship('Genre', secondary='book_genres')
    
    def __repr__(self):
        return f"<Book(title={self.title}, year={self.publication_year}, author={self.author.name})>"

# Association table for Many-to-Many between Book and Genre
class BookGenres(Base):
    __tablename__ = 'book_genres'
    
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)


DATABASE_URL = "sqlite:///readkeeer.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)