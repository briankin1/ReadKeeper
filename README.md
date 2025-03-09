             # ReadKeeper

##Overview
ReadKeeper is a command-line interface (CLI) application that helps users manage their personal book collection. Users can add, view, update, and delete books in their library, as well as categorize books by genre and author. This application leverages SQLAlchemy for database management, and it is built using Python to demonstrate various programming concepts such as object-oriented programming (OOP), data structures, and SQL relations.


##Table of Contents
1. Installation
2. Usage
3. Project Structure
4. CLI Commands
5. Models
6. Dependencies

##Installation

To set up ReadKeeper application, follow the steps below:

 1. Clone the repository:
```bash
git clone https://github.com/briankin1/ReadKeeper.git
cd personal-library-manager
```bash

 2. Create a virtual environment (recommended to avoid conflicts with global Python packages):
```bash
pipenv install
```bash

 3. Install the dependencies
```bash
pipenv install --dev
```bash

 4. Set up the database: After installing dependencies, run Alembic migrations to create the database schema:
```bash
alembic upgrade head
```bash

 5. Run the application: Once the environment is set up and migrations are applied, you're ready to use the CLI application.


##Usage

Once the environment is set up, you can interact with the application through the command line. The available commands are described in the CLI Commands section.

To run the application, use the following command:
```bash
python main.py <command>
```bash

##Project Structure

Here’s an overview of the project files and their purpose:

```bash
personal-library-manager/
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
```bash








