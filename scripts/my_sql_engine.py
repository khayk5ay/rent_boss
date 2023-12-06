# Import necessary packages
import MySQLdb
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Establish environment variables
user=os.environ["SQL_USERNAME"]
password=os.environ["SQL_PASS"]

# Connect to the DBMS using SQLAlchemy

class Engine:

    def __init__(self, database_name):
        self.database_name = database_name

    def make_engine(self):
        return(create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{self.database_name}", echo=True))


Base = declarative_base()
