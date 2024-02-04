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

# Define functions

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")



# Define Main function
def main():
    db_filepath = 'project.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'create_tables.sql')
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")


# Conditional script
if __name__ == '__main__':
    main()