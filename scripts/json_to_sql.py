from my_sql_engine import Engine
from sqlalchemy import create_engine, text
import pandas as pd

# Connect to database
engine_object = Engine("rentboss")

engine= engine_object.make_engine()

connection = engine.connect()


# Create dataframe from json file
airbnb_admin_info = pd.read_json('./admin_info.json')

print(airbnb_admin_info)

airbnb_admin_info.to_sql(name='admin_info_2', con = connection)
