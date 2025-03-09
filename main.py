import click
from models import Author, Book, Genre, Session, create_tables

# Create tables
create_tables()

# Function to get the session
def get_session():
    return Session()

@click.group()
def cli():
    pass

# Add Book command
@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author', prompt='Author name', help='The author of the book.')
@click.option('--year', prompt='Publication year', help='The year the book was published.')
@click.option('--genres', prompt='Genre IDs (comma separated)', help='Comma-separated genre IDs.')
def add_book(title, author, year, genres):
    session = get_session()

    # Get or create the author
    author_obj = session.query(Author).filter_by(name=author).first()
    if not author_obj:
        author_obj = Author.create(session, author)

    genre_ids = [int(gid) for gid in genres.split(',')]
    book = Book.create(session, title, year, author_obj.id, genre_ids)

    click.echo(f"Book '{book.title}' by {book.author.name} added.")

# List all books
@click.command()
def list_books():
    session = get_session()
    books = Book.get_all(session)
    for book in books:
        click.echo(f"{book.title} by {book.author.name} ({book.publication_year})")
    
# Update Book command
@click.command()
@click.option('--id', prompt='Book ID', help='The ID of the book to update.')
@click.option('--title', prompt='New book title', help='The new title of the book.')
def update_book(id, title):
    session = get_session()
    book = Book.find_by_id(session, id)
    if book:
        book.title = title
        session.commit()
        click.echo(f"Book {id} updated to '{title}'")
    else:
        click.echo(f"Book {id} not found.")

# Delete Book command
@click.command()
@click.option('--id', prompt='Book ID', help='The ID of the book to delete.')
def delete_book(id):
    session = get_session()
    if Book.delete(session, id):
        click.echo(f"Book {id} deleted.")
    else:
        click.echo(f"Book {id} not found.")

# Add Author command
@click.command()
@click.option('--name', prompt='Author name', help='The name of the author.')
def add_author(name):
    session = get_session()
    author = Author.create(session, name)
    click.echo(f"Author '{author.name}' added.")

# List Authors command
@click.command()
def list_authors():
    session = get_session()
    authors = Author.get_all(session)
    for author in authors:
        click.echo(f"{author.name}")

# Add Genre command
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    session = get_session()
    genre = Genre.create(session, name)
    click.echo(f"Genre '{genre.name}' added.")

# List all Genres command
@click.command()
def list_genres():
    session = get_session()
    genres = Genre.get_all(session)
    if genres:
        for genre in genres:
            click.echo(f"Genre: {genre.name}")
    else:
        click.echo("No genres found.")

# View Books by Genre command
@click.command()
@click.option('--genre_id', prompt='Genre ID', help='The ID of the genre to view books for.')
def view_books_by_genre(genre_id):
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
