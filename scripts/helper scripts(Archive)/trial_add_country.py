import requests
import numpy as np

url = "https://airbnb-listings.p.rapidapi.com/v2/getadmins"

querystring = {"countrycode":"NG"}

headers = {
	"X-RapidAPI-Key": "093e8a5f8dmsh77117076185e6d7p19193bjsn4d285fc8da17",
	"X-RapidAPI-Host": "airbnb-listings.p.rapidapi.com"
}

#response = requests.get(url, headers=headers, params=querystring)
results = response.json()["results"]

results_np
print(results_np)
