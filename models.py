# This is the main database for my ReadKeeper app
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors' # keeping it simple
    
    # basic author info 
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # this part should probably add unique=True
    
    # One-to-many relationship - links specific author to their books lol
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return f"<Author(name={self.name})>" # for debugging

    # ORM Methods - Might consider spliting this into a separate file?
    @classmethod
    def create(cls, session, name):
        # quick way to add new authors
        author = cls(name=name)
        session.add(author)
        session.commit()
        return author

    @classmethod
    def delete(cls, session, author_id):
        author = session.query(cls).get(author_id)
        if author:
            session.delete(author)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        # returns everything
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, author_id):
        # simple lookup by id
        return session.query(cls).get(author_id)


class Genre(Base):
    __tablename__ = 'genres'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False) # should add unique constraint ?
    
    # Many-to-many relationship- links books to many genres
    books = relationship("Book", secondary="book_genres", back_populates="genres")


    def __repr__(self):
        return f"<Genre(name={self.name})>"

    
    @classmethod
    def create(cls, session, name):
        genre = cls(name=name)
        session.add(genre)
        session.commit()
        return genre

    @classmethod
    def delete(cls, session, genre_id):
        genre = session.query(cls).get(genre_id)
        if genre:
            session.delete(genre)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, genre_id):
        return session.query(cls).get(genre_id)


class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    
    # Relationships - took me a while to get right
    author = relationship("Author", back_populates="books")
    genres = relationship("Genre", secondary="book_genres", back_populates="books")


    def __repr__(self):
        #added author name for debbugging output
        return f"<Book(title={self.title}, year={self.publication_year}, author={self.author.name})>"

    
    @classmethod
    def create(cls, session, title, publication_year, author_id, genre_ids):
        # Creates new book instance
        book = cls(title=title, publication_year=publication_year, author_id=author_id)
        session.add(book)
        session.commit()

        # This Adds genres to a book 
        for genre_id in genre_ids:
            genre = session.query(Genre).get(genre_id)
            if genre: # makes sure genre exists] maybe should raise error?
                book.genres.append(genre)
        session.commit() # commit again for genres
        return book

    @classmethod
    def delete(cls, session, book_id):
        # now this is a straightforward delete
        book = session.query(cls).get(book_id)
        if book:
            session.delete(book)
            session.commit()
            return True
        return False

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, book_id):
        return session.query(cls).get(book_id)
    
    @classmethod
    def update(cls, session, book_id, title=None, publication_year=None, author_id=None, genre_ids=None):
        book = cls.find_by_id(session, book_id)
        if not book:
            return None

        # Updates whatever fields are passed
        if title: book.title = title 
        if publication_year: book.publication_year = publication_year
        if author_id: book.author_id = author_id
        # genre updates still - quite annoying to handle
        if genre_ids is not None:
            book.genres.clear() # resets genres
            for genre_id in genre_ids:
                genre = session.query(Genre).get(genre_id)
                if genre:
                    book.genres.append(genre)

        session.commit()
        return book


# junction table for the many-to-many relationship btwn books $ genres
class BookGenres(Base):
    __tablename__ = 'book_genres'
    
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)

DATABASE_URL = "sqlite:///readkeeer.db"   # my database url here

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    # Creates all tables - run this when setting up db, once though!
    Base.metadata.create_all(engine)