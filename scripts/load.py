"""
This script uploads the files in sql tables

"""

import os
from dotenv import load_dotenv
from my_sql_engine import Engine
from sqlalchemy import create_engine, text, DateTime, String
import pandas as pd
#import datetime

base_path = os.environ["BASE_DIR"]

def csv_to_sql():
    # Connect to database
    engine_object = Engine("rentboss")

    engine= engine_object.make_engine()

    connection = engine.connect()

    for file in os.listdir(f"{base_path}/data"):
        if file.endswith(".csv"):
            table_name = file.split(".")[0]
            df = pd.read_csv(f"{base_path}/data/{file}")
            df.to_sql(name = table_name, con= connection, if_exists="replace",
                      dtype={"airbnb_id": String(64), "last_avail_check": DateTime, "last_updated": DateTime,  "last_ratings":DateTime})



def main():
    csv_to_sql()


main()
