# CLI file for my book my personal book collection

import click
from models import Author, Book, Genre, Session, engine, create_tables
from sqlalchemy.orm import sessionmaker

# Db connection thing
Session = sessionmaker(bind=engine)
session = Session()

# initialize db tables
create_tables()

# This is a get session function just incase
def get_session():
    return Session()

@click.group()
def cli():

    pass


@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author', prompt='Author name', help='The author of the book.')
@click.option('--year', prompt='Publication year', help='The year the book was published.')
@click.option('--genres', prompt='Genre IDs (comma separated)', help='Comma-separated genre IDs.')
def add_book(title, author, year, genres):
    """add a new book to readkeeper manager"""
    session = get_session()

    # First create author if it doesnt exist
    author_obj = session.query(Author).filter_by(name=author).first()
    if not author_obj:
        author_obj = Author.create(session, author)

    genre_ids = [int(gid) for gid in genres.split(',')]
    book = Book.create(session, title, year, author_obj.id, genre_ids)

    click.echo(f"Book '{book.title}' by {book.author.name} added.")


@click.command()
def list_books():
    """shows all books in db"""
    session = get_session()
    books = Book.get_all(session)
    for book in books:
        click.echo(f"{book.title} by {book.author.name} ({book.publication_year})")
    

@click.command()
@click.option('--id', prompt='Book ID', help='ID of the book to update.')
@click.option('--title', prompt='New Title', help='New title of the book.')
@click.option('--author', prompt='New Author', help='New author of the book.')
@click.option('--year', prompt='New Publication Year', help='New publication year of the book.', type=int)
@click.option('--genres', prompt='New Genre IDs', 
              help='Comma separated list of genre IDs to associate with the book.', type=str)
def update_book(id, title, author, year, genres):
    """Update existing book details"""
    # might need refactoring but glad it works
    book = session.query(Book).filter(Book.id == id).first()

    if not book:
        click.echo(f"Cant find book #{id}") # Error handling
        return

    # Updates everything - book details
    book.title = title
    book.author.name = author  
    book.publication_year = year

    # deal with genres only if provided
    if genres:
        genre_ids = [int(genre_id.strip()) for genre_id in genres.split(',')]
        genres_to_add = session.query(Genre).filter(Genre.id.in_(genre_ids)).all()
        book.genres = genres_to_add

    
    session.commit()
    click.echo(f"Updated book #{id}")



@click.command()
@click.option('--id', prompt='Book ID', help='The ID of the book to delete.')
def delete_book(id):
    """remove a book from db"""
    session = get_session()
    if Book.delete(session, id):
        click.echo(f"Book {id} deleted.")
    else:
        click.echo(f"Book {id} not found.")


@click.command()
@click.option('--name', prompt='Author name', help='The name of the author.')
def add_author(name):
    """add new author"""
    session = get_session()
    author = Author.create(session, name)
    click.echo(f"Author '{author.name}' added.")


@click.command()
def list_authors():
    """shows all authors"""
    session = get_session()
    authors = Author.get_all(session)
    for author in authors:
        click.echo(f"{author.name}")


@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    """add new genre"""
    session = get_session()
    genre = Genre.create(session, name)
    click.echo(f"Genre '{genre.name}' added.")


@click.command()
def list_genres():
    """List all avaible genres"""
    session = get_session()
    genres = Genre.get_all(session)
    if genres:
        for genre in genres:
            click.echo(f"Genre: {genre.name}") # can maybe add id here too?
    else:
        click.echo("No genres yet!")


@click.command()
@click.option('--genre_id', prompt='Genre ID', help='The ID of the genre to view books for.')
def view_books_by_genre(genre_id):
    """View all books in a specific genre"""
    session = get_session()
    genre = Genre.find_by_id(session, genre_id)
    if genre:
        click.echo(f"Books in the genre '{genre.name}':")
        if genre.books:
            for book in genre.books:
                click.echo(f"- {book.title} by {book.author.name} ({book.publication_year})")
        else:
            click.echo("No books found for this genre.")
    else:
        click.echo(f"Genre with ID {genre_id} not found.")

# Registering all the commands here
cli.add_command(add_book)
cli.add_command(list_books)
cli.add_command(update_book)
cli.add_command(delete_book)
cli.add_command(add_author)
cli.add_command(list_authors)
cli.add_command(add_genre)
cli.add_command(list_genres)
cli.add_command(view_books_by_genre)

if __name__ == '__main__':
    cli()

# IDEAS i MIGHT have to do later
#- add search functionality
#- fix the weird authour update stuff
#- add better error handling

