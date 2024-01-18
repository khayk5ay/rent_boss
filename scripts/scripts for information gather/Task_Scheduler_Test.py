
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
start_date = datetime.datetime.strptime("2024-01-18", "%Y-%m-%d")

current_date = datetime.datetime.today()
current_date_string = datetime.datetime.strftime(current_date, "%Y-%m-%d")

# Increase the offset based on the number of days. first day will be 0, second day will be 50, third will be 100
offset_number = int(current_date.day - start_date.day) * 50
offset = str(offset_number)


"""
#TASK 1
"""
# Only perform on the first day
if offset_number == 0:
    for c in countries: 
        extract.get_admin_info(country=c)

