""" I will connect to the Airbnb API and extract basic information on administrative regions in West Africa"""

# Import necessary packages

import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import datetime

# Load environment variables

load_dotenv()
base_path = os.environ["BASE_DIR"]+"/data/prelim"


headers = {
	"X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
	"X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
}

os.makedirs(base_path, exist_ok=True)


# Get a list of the country codes that we will be using
countries = pd.read_csv(f"{base_path}/countries.csv")["country_code"].str.strip()

def response_to_json(response, path, use=1, country="NA", listing_id="NA"):
    
    # Extract the results from the get request response
    results = response.json()["results"]

    if use == 1:
        
        # Add a key value pair to specify the country for each entry
        # This is necessary because each json file will contain information for multiple countries
        for i in results:
            i["country"] = country
    elif use == 2:

        # Add a key value pair to specify the listing id for each entry
        # This is necessary because each json file will contain information for listings
        for i in results:
            i["listing_id"] = listing_id
        

    # Extend the already exisitng json file with new country information 
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


def get_admin_info(url= "https://airbnb-listings.p.rapidapi.com/v2/getadmins", country="GH"):

    # Specify the file name
    filename = "admin_info.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename

    querystring = {"countrycode":country}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, use=1, country=country)
    


def get_listing_by_georef(url = "https://airbnb-listings.p.rapidapi.com/v2/listingsByGeoRef", country="NG", offset="0", date_string="2024-01-18"):
    
    # Specify the file name
    filename = "listing_georef.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename

    querystring = {"state":country, "offset":offset}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, use=1, country=country)


def get_listing_reviews(listing_id, url = "https://airbnb-listings.p.rapidapi.com/v2/listingReviews"):

    # Specify the file name
    filename = "listing_reviews.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename
    
    querystring = {"id":str(listing_id)}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, use=2, listing_id=listing_id)   


def get_listing_descriptions(listing_id, url="https://airbnb-listings.p.rapidapi.com/v2/listing"):
    
    # Specify the file name
    filename = "listing_descriptions.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename
    
    querystring = {"id":str(listing_id)}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, use=2, listing_id=listing_id)
    




            



