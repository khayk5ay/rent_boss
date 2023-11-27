"""
    This script contains functions to work on the csv files created from the get requests.
    They are specifically tailored to each of the files and the format of the data

"""

import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def admin_info_transform():

    pass

def listing_georef_transform():
    base_path = os.environ["BASE_DIR"]
    listing_georef = pd.read_csv(f"{base_path}/data/listing_georef.csv", parse_dates=["last_updated", "last_avail_check", "last_ratings"], index_col=0, dtype={"airbnb_id":str})
    listing_georef.to_csv(f"{base_path}/data/listing_georef_clean.csv")



def main():
    admin_info_transform()
    listing_georef_transform()
