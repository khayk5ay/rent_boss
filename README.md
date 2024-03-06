This project is called Rent Boss

It is basically an accommodation booking/rental service [Kinda like Arirbnb].

The project is basically to showcase my skills in Data Engineering and how I can develope a data pipeline from scratch.

The data used in the project is gotten from Airbnb through RapidAPI.
I focused on accommodation in 7 specific countries in West Africa.

extract.py
This script contains the API calls to collect certain information about the properties
-The administrative regions and names in each of the countries
-The listing IDs of listings in the countries
-The listing ratings of the listings
-The listing reviews 

transform.py
This script converts the information saved in json files to csv files and cleans the data to ensure that it is easily ingested into the database
- Null values in admin_info are replaced with relevant values

  
load.py
Here, all csv files in the data folder are loaded into the already existing database
-The column datatypes are specified
-The column constraints are specified

Code Climate Maintainability

[![Maintainability](https://api.codeclimate.com/v1/badges/1d49865c936e74b1b8e2/maintainability)](https://codeclimate.com/github/khayk5ay/rent_boss/maintainability)
