"""
    Define the python classes that correspond to the SQL tables for our rentboss datatbase
"""

from my_sql_engine import Engine, Base
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy import Column, Integer, String, DateTime



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


