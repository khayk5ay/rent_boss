""" I will connect to the Airbnb API and extract basic information on Listing status for all the listings in the selected countries"""

# Import necessary packages

import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables

load_dotenv()

url = "https://airbnb-listings.p.rapidapi.com/v2/listingsByGeoRef"

querystring = {"state":"GH", "offset":"0"}

headers = {
	"X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
	"X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
}

response = requests.get(url, headers=headers, params=querystring)


# print(response.json()["results"])
try:
    with open("listings_by_georef.json", "r") as f:
        info = json.load(f)
        info.extend(response.json()["results"])
    with open("listings_by_georef.json", "w") as f:
        json.dump(info, f)

except:
    with open("listings_by_georef.json", "w") as f:
        json.dump(response.json()["results"], f)


    



