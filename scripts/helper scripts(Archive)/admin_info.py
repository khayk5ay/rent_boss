""" I will connect to the Airbnb API and extract basic information on administrative regions in Italy """

# Import necessary packages

import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables

load_dotenv()
base_path = os.environ["BASE_DIR"]
filename = "admin_info.json"
data_path = base_path+"/"+filename

print(data_path)

url = "https://airbnb-listings.p.rapidapi.com/v2/getadmins"

querystring = {"countrycode":"GH"}

headers = {
	"X-RapidAPI-Key": os.environ["RAPID_API_KEY"],
	"X-RapidAPI-Host": os.environ["RAPID_API_HOST"]
}

response = requests.get(url, headers=headers, params=querystring)



# print(response.json()["results"])
try:
    with open(data_path, "r") as f:
        info = json.load(f)
        info.extend(response.json()["results"])
    with open(data_path, "w") as f:
        json.dump(info, f)

except:
    with open(data_path, "w") as f:
        json.dump(response.json()["results"], f)


    



