""" I will connect to the Airbnb API and extract basic information on administrative regions in Italy """

# Import necessary packages

import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables

load_dotenv()

url = "https://airbnb-listings.p.rapidapi.com/v2/getadmins"

querystring = {"countrycode":"IT","admin1":"07","admin2":"RM","admin3":"058091","admin4":"05809101"}

headers = {
	"X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
	"X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
}

response = requests.get(url, headers=headers, params=querystring)

with open("admin_info.json", "w") as f:
	json.dump(response.json()["results"], f)



