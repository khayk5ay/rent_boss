"""
For this file, each API call returns a single record, therefore i have a limited number of calls per day
However, I want to use the declarative base class of SQLAlchemy to insert the records directly into the SQL database
As opposed to using the pandas to_sql method like i did in the other set of data
"""

from SQLAlchemy import Declarative_Base
import os
from dotenv import load_dotenv

