"""
For this file, each API call returns a single record, therefore i have a limited number of calls per day
However, I want to use the declarative base class of SQLAlchemy to insert the records directly into the SQL database
As opposed to using the pandas to_sql method like i did in the other set of data
"""

from my_sql_engine import Engine, Base
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import os
from dotenv import load_dotenv


engine_object = Engine("rentboss")

engine = engine_object.make_engine()

session = Session(engine)


class ListingReviews(Base):
    __tablename__ = "listing_reviews"
    review_id = Column(Integer, primary_key = True)
    comments = Column(String(555))
    response = Column(String(255))
    date_time = Column(DateTime)
    language = Column(String(8))
    rating = Column(Integer)
    guest_id = Column(Integer)
    
    
