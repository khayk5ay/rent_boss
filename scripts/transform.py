"""
    This script contains functions to work on the csv files created from the get requests.
    They are specifically tailored to each of the files and the format of the data

"""

import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

base_path = os.environ["BASE_DIR"]

def admin_info_transform():
    file_path = base_path+"/data/admin_info.json"

    df = pd.read_json(file_path)
    df.admin1_name = np.where(df["admin1_name"] == "n/a", df["admin1"], df["admin1_name"])
    df = df.drop_duplicates()
    

def listing_georef_transform():

    file_path = base_path+"/data/listings_georef.json"

    df = pd.read_json(file_path)
    df = df.drop_duplicates()
    pass

def listing_reviews_transform():
    file_path = base_path+"/data/listing_reviews.json"

    df = pd.read_json(file_path)
    df = df.drop_duplicates()

    # Remove the unwanted quotations marks surrounding the text
    df.comments = df.comments.str[1:-1]
    df.response = df.response.str[:-1]
    df.response = df.response.str[1:]

    pass

def listing_descriptions_transform():
    file_path = base_path+"/data/listing_descriptions.json"

    df = pd.read_json(file_path)
    df = df.drop_duplicates()
    
    pass

def main():
    admin_info_transform()
    listing_georef_transform()
    
