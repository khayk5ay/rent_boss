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

def pd_to_json(dataframe, path):

    dataframe.to_json(path)
    print(f"New file saved at {path}")


def admin_info_transform():
    
    file_path = base_path+"/data/admin_info.json"

    df = pd.read_json(file_path)
    df.admin1_name = np.where(df["admin1_name"] == "n/a", df["admin1"], df["admin1_name"])
    df = df.drop_duplicates()

    # Create new file name for the transformed data
    new_file_path = file_path.replace(".json", "_new.json")

    # Save the new dataframe in a json file
    pd_to_json(df, new_file_path)
    

def listing_georef_transform():

    file_path = base_path+"/data/listing_georef.json"

    # Save the data in a dataframe
    df = pd.read_json(file_path)

    # Remove any duplicates
    df = df.drop_duplicates()

    # Create new file name for the transformed data
    new_file_path = file_path.replace(".json", "_new.json")

    # Save the new dataframe in a json file
    pd_to_json(df, new_file_path)
    

def listing_reviews_transform():
    file_path = base_path+"/data/listing_reviews.json"

    # Save the data in a dataframe
    df = pd.read_json(file_path)

    # Remove any duplicates
    df = df.drop_duplicates()

    # Remove the unwanted quotations marks surrounding the text
    df.comments = df.comments.str[1:-1]
    df.response = df.response.str[:-1]
    df.response = df.response.str[1:]

    # Create new file name for the transformed data
    new_file_path = file_path.replace(".json", "_new.json")

    # Save the new dataframe in a json file
    pd_to_json(df, new_file_path)

    

def listing_descriptions_transform():
    file_path = base_path+"/data/listing_descriptions.json"

    
    # Save the data in a dataframe
    df = pd.read_json(file_path, dtype={"listing_id": str})

    # Remove any duplicates
    df = df.drop_duplicates()

    # Keep only needed columns
    descriptions_df = df[['listing_id', 'listingTitle', 'isSuperhost', 'reviewCount',
                              'starRating', 'maxGuestCapacity', 'propertyType', 'listingstatus']]

    # Fill missing values in superhost column with 0 then change column type to boolean
    descriptions_df.isSuperhost = descriptions_df.isSuperhost.fillna(0).astype(bool)

    # Create new file name for the transformed data
    new_file_path = file_path.replace(".json", "_new.json")

    # Save the new dataframe in a json file
    pd_to_json(descriptions_df, new_file_path)

    
    # Create new table- lissting_locations
    locations_df = df[['listing_id', 'city', 'listingLat','listingLng', 'market']]
    
    # Create new file name for the transformed data
    new_file_path = base_path+"/data/listing_locations_new.json"

    # Save the new dataframe in a json file
    pd_to_json(locations_df, new_file_path)


def main():
    admin_info_transform()
    listing_georef_transform()
    listing_reviews_transform()
    listing_descriptions_transform()
    
