# Import necessary packages

import os
from dotenv import load_dotenv
import csv
import pandas as pd
import datetime


import extract

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

# Collect information for all the countries for our database and analysis [West Africa]
start_date = datetime.datetime.strptime("2024-01-13", "%Y-%m-%d")

current_date = datetime.datetime.today()
current_date_string = datetime.datetime.strftime(current_date, "%Y-%m-%d")

# Increase the offset based on the number of days. first day will be 0, second day will be 50, third will be 100
offset_number = int(current_date.day - start_date.day)
offset = str(offset_number*50)
day = offset_number+1
print(f"This is Day {day}") 
print(f"Starting from number {offset}")


"""
#TASK 1
"""
# Only perform on the first day
if offset_number == 0:
    for c in countries: 
        extract.get_admin_info(country=c)


    
"""
#TASK 2
"""
# Only perform for the first 10 days
if offset_number < 10:    
    for c in countries:
        print(f"Extracting {c} for Day {offset_number + 1}")
        extract.get_listing_by_georef(country=c, offset=offset, date_string=current_date_string)


"""
TASK 3
"""
# Only start after the 10th day
if offset_number>=10:
    # Only listings with 8 digit listing ID should be queried for reviews .and descriptions
    listings_raw = pd.read_json(f"{base_path}/listing_georef.json")
    
    #Filter listings for IDs that have reviews and descriptions (Only IDs less than 9 digits)
    listings = listings_raw[(listings_raw["airbnb_id"]).astype(str).str.len() < 9].reset_index(drop=True)

    
    # Create start and end for looping through the dataframe, for offset 10, the request will start from the first listing in the dataframe [(10-10) * 20 = 0]
    # for the offset 11, the request will start from the 21st listing in the dataframe [(11-10) * 20 = 20], and so on...
    task_start = (offset_number-10) * 20
    
    task_end = task_start + 20

    # Check if within the range of the dataframe, else change the end to the dataframe length
    if task_end >= len(listings):
        task_end = len(listings)

        
    for each in range(task_start, task_end):
        #For each listing in the selected range for the day, get the listing reviews and the listing description
        extract.get_listing_reviews(str(listings.iloc[each,0]))
        extract.get_listing_descriptions(str(listings.iloc[each,0]))

        
        
