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
