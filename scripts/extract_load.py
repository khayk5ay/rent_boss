"""
For this file, each API call returns a single record, therefore i have a limited number of calls per day
However, I want to use the declarative base class of SQLAlchemy to insert the records directly into the SQL database
As opposed to using the pandas to_sql method like i did in the other set of data
"""

import os
from dotenv import load_dotenv
import requests
import pandas as pd
import json

load_dotenv()
base_path = os.environ["BASE_DIR"]+"/data"

headers = {
            "X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
            "X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
            }

def response_to_json(response, path, listing_id):
    
    # Extract the results from the get request response
    try:
        results = response.json()["results"]
        

    except:
        # If there are no reviews for that listing, convert the response to a json by making it a list of dicts
        results = [response.json()]

        
    # Add a key value pair to specify the country for each entry
    # This is necessary because each json file will contain information for multiple countries   
    for i in results:
            i["listing_id"] = listing_id    

    # Extend the already exisitng json file with listing review information 
    try:
        with open(path, "r") as f:
            info = json.load(f)
            info.extend(results)
        with open(path, "w") as f:
            json.dump(info, f)
            
    # Create a new json file for the information and insert the results of the response
    except:
        with open(path, "w") as f:
            json.dump(results, f)

            
def get_listing_reviews(listing_id, url = "https://airbnb-listings.p.rapidapi.com/v2/listingReviews"):

    # Specify the file name
    filename = "listing_reviews.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename
    
    querystring = {"id":str(listing_id)}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, listing_id=listing_id)   


def get_listing_descriptions(listing_id, url="https://airbnb-listings.p.rapidapi.com/v2/listing"):
    
    # Specify the file name
    filename = "listing_descriptions.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename
    
    querystring = {"id":str(listing_id)}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, listing_id=listing_id)
    

# Only listings with 8 digit listing ID should be queired for reviews .and descriptions
listings_raw = pd.read_csv(f"{base_path}/listing_georef.csv", usecols=[1])

#Filter listings for IDs that have reviews and descriptions (Only IDs less than 9 digits)
listings = listings_raw[(listings_raw["airbnb_id"]).astype(str).str.len() < 9]


for each in listings.values:
    # "each" returns a numpy array therefore we need to collect the listing id as the first element in the array
    # The listing id is needed in string format therefore we need to then convert the listing id to string
    get_listing_reviews(str(each[0]))
    get_listing_descriptions(str(each[0]))

