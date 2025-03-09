# ReadKeeper

## Overview

ReadKeeper is a command-line interface (CLI) application that helps users manage their personal book collection. Users can add, view, update, and delete books in their library, as well as categorize books by genre and author. This application leverages SQLAlchemy for database management, and it is built using Python to demonstrate various programming concepts such as object-oriented programming (OOP), data structures, and SQL relations.


## Table of Contents
1. Installation
2. Usage
3. Project Structure
4. CLI Commands
5. Models
6. Dependencies


## Installation

To set up ReadKeeper application, follow the steps below:


 1. Clone the repository:
    ```bash
    git clone https://github.com/briankin1/ReadKeeper.git
    cd personal-library-manager
    ```
    


 2. Create a virtual environment (recommended to avoid conflicts with global Python packages):
    ```bash
    pipenv install
    ```


 3. Install the dependencies
    ```bash
    pipenv install --dev
    ```

 4. Set up the database: After installing dependencies, run Alembic migrations to create the database schema:
    ```bash
    alembic upgrade head
    ```


 5. Run the application: Once the environment is set up and migrations are applied, you're ready to use the CLI application.


## Usage

Once the environment is set up, you can interact with the application through the command line. The available commands are described in the CLI Commands section.

To run the application, use the following command:

```bash
    python main.py <command>
 ```


## Project Structure

Here’s an overview of the project files and their purpose:

```bash
    ReadKeeper/
│
├── alembic/                    # Alembic migrations folder (auto-generated)
│
├── models.py                   # Contains the data models (Book, Author, Genre)
│
├── main.py                     # Main entry point for the CLI application
│
├── requirements.txt            # Lists the Python packages required for the project
│
├── Pipfile                     # Pipenv virtual environment configuration
│
├── Pipfile.lock                # Pipenv lock file for dependencies
│
├── README.md                   # This file
│
└── migrations/                 # Alembic migration scripts folder
```

   
     



## main.py

The main.py file is the starting point of the CLI application. It imports and runs the main.py commands using the Click library. This file handles the setup and execution of the CLI script.
The file defines the user interface and interactions with the user. It uses the Click library to create commands that the user can run in the terminal. Each command is designed to manage the library’s books, authors, and genres.

## Key functions include:

add_book: Adds a new book to the library.

list_books: Displays all books in the library.

update_book: Allows updating details of a book (title, year, genres).

delete_book: Deletes a book from the library.

add_author: Adds a new author to the library.

list_authors: Lists all authors.

add_genre: Adds a genre to the library.

list_genres: Lists all genres.


## models.py

The models.py file defines the data models for the application. These models represent the database schema and the relationships between books, authors, and genres.

## Key models include:

Book: Represents a book in the library with attributes like title, publication_year, author, and genres.

Author: Represents an author with a name and a relationship to the books they’ve written.

Genre: Represents a genre with a name and a relationship to the books that belong to the genre.

Each model is built using SQLAlchemy’s Object-Relational Mapping (ORM) system, which allows interaction with the database through Python objects. Methods such as create, update, delete, and get_all are provided for each model to handle common CRUD operations.


## CLI Commands

Here are the main CLI commands available for managing your ReadKeeper:

## Books

1. Add a new book:
    ```bash
    python main.py add-book --title "1984" --author "George Orwell" --year 1949 --genres 1,2
    ```

   Adds a new book with the specified title, author, year, and genres.


2. List all books:
     ```bash
    python main.py list-books
     ```

   lists all the books in the library


3. Update book:

    ```bash
    python main.py update-book --id 1 --title "Nineteen Eighty-Four" --year 1950
    ```

    Updates the title and year of the book with the specified ID.


4. Delete book:
    ```bash
    python main.py delete-book --id 1
    ```

    Deletes the book with the specied ID


5. Authors
  
   Add a new author:
    ```bash
    python main.py add-author --name "Osho"
    ```

   Lists all authors in the library.


6. Genres

   Add a new genre:

    ```bash
    python main.py add-genre --name "Dystopian"
   ```

   Adds a new author with the name


7. list genres:
    
    ```bash
    python main.py list-genres
    ```

    Lists all genres in the library.


## Models

## Book Model (Defined in models.py)

## Attributes:

 id: Integer (Primary Key)

 title: String (Title of the book)

 publication_year: Integer (Year the book was published)

 author_id: Integer (Foreign Key to the authors table)

 author: Relationship with the Author model

 genres: Relationship with the Genre model through the book_genres table


## Methods:

 create: Creates a new book and saves it to the database.

 get_all: Retrieves all books from the database.

 find_by_id: Retrieves a book by its ID.

 delete: Deletes a book from the database.

 update: Updates a book’s details.

 Author Model (Defined in models.py)

## Attributes:

 id: Integer (Primary Key)

 name: String (Name of the author)

 books: Relationship with the Book model

## Methods:

 create: Adds a new author.

 get_all: Retrieves all authors.

 find_by_id: Retrieves an author by ID.

 delete: Deletes an author.

 Genre Model (Defined in models.py)

## Attributes:

 id: Integer (Primary Key)

 name: String (Name of the genre)

 books: Relationship with the Book model

## Methods:

 create: Adds a new genre.

 get_all: Retrieves all genres.

 find_by_id: Retrieves a genre by ID.

 delete: Deletes a genre.


## Dependencies

SQLAlchemy: ORM for managing the database and defining relationships.

Alembic: Database migration tool used to generate and apply schema changes.

Click: A Python package used for building command-line interfaces.

Pipenv: Dependency management tool for managing Python environments.

To install dependencies, run the following command:

```bash
pipenv install
```

## License

This project is licensed under the MIT License.

## Contact

Mail to: brianmkcnight@gmail.com
























