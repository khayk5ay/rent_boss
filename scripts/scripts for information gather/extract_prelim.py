""" I will connect to the Airbnb API and extract basic information on administrative regions in West Africa"""

# Import necessary packages

import os
from dotenv import load_dotenv
import requests
import json
import csv
import pandas as pd
import datetime

# Load environment variables

load_dotenv()
base_path = os.environ["BASE_DIR"]+"/data"


headers = {
	"X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
	"X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
}

os.makedirs(base_path, exist_ok=True)


# Get a list of the country codes that we will be using
countries = pd.read_csv(f"{base_path}/countries.csv")["country_code"].str.strip()


def response_to_json(response, path, country):
    
    # Extract the results from the get request response
    results = response.json()["results"]

    
    # Add a key value pair to specify the country for each entry
    # This is necessary because each json file will contain information for multiple countries
    for i in results:
        i["country"] = country

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
      
    

def get_admin_info(url= "https://airbnb-listings.p.rapidapi.com/v2/getadmins", country="GH"):

    # Specify the file name
    filename = "admin_info.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename

    querystring = {"countrycode":country}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, country=country)
    
   
def get_listing_by_georef(url = "https://airbnb-listings.p.rapidapi.com/v2/listingsByGeoRef", country="NG", offeset="0"):

    # Specify the file name
    filename = "listing_georef.json"

    # Specify the path to the file
    data_path = base_path+"/"+filename

    querystring = {"state":country, "offset":"0"}

    # Make request to the API and save the response
    response = requests.get(url, headers=headers, params=querystring)

    # Convert the results from the get request to a json file
    response_to_json(response=response, path=data_path, country=country)


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
    



def main():

    # Collect information for all the countries for our database and analysis [West Africa]
    start_date = datetime.datetime.strptime("2024-01-10", "%Y-%m-%d")

    current_date = datetime.datetime.today()

    offset = str(int(current_date.day - start_date.day))
    
    for c in countries: 
        get_admin_info(country=c)
        get_listing_by_georef(country=c, offset=offset)

    # Only listings with 8 digit listing ID should be queried for reviews .and descriptions
    listings_raw = pd.read_csv(f"{base_path}/listing_georef.csv", usecols=[1])

    #Filter listings for IDs that have reviews and descriptions (Only IDs less than 9 digits)
    listings = listings_raw[(listings_raw["airbnb_id"]).astype(str).str.len() < 9]


    for each in listings.values:
        # "each" returns a numpy array therefore we need to collect the listing id as the first element in the array
        # The listing id is needed in string format therefore we need to then convert the listing id to string
        get_listing_reviews(str(each[0]))
        get_listing_descriptions(str(each[0]))






            



