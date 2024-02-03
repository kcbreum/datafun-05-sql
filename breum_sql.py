'''
Project 5 - SQL Module
This script should demonstrate the ability to interact with a SQL database, including creating a database, defining a schema, and executing various SQL commands. 
Logging is incorporated to document the process and provide user feedback.

Author: Kayla Breum, guided by Denise Case
'''

# Import dependencies
import csv
from pathlib import Path
import sqlite3
import uuid
import pandas as pd
import pyarrow
from io import StringIO
import requests



# Configure logging
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")


# Define the database file in the current root project directory
db_file = Path("project.sqlite3")
def create_database():
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

# Create tables for databases
def insert_data_from_csv():
    try:
        author_data_path = Path("data", "authors.csv")
        book_data_path = Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)



# Define main
def main():
    create_database()
    insert_data_from_csv()

if __name__ == "__main__":
    main()