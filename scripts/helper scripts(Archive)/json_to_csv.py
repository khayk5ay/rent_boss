import pandas as pd
import numpy as np
import os



def json_to_csv(filename, base_path = r"C:\Users\K84277516.CHINA\Documents\KAINE DATA PROJECTS\rent_boss_parody\data"):
    """
        Function to convert the contents of a json file located in the data directory to a csv file with the same name and in the same directory
    """
          
    # Combine the base path and the file name provided to get the full file path
    filepath = base_path+"/" + filename

    # Convert the JSON file into a pandas dataframe
    df = pd.read_json(filepath)

    # Generate the filepath for the csv file. It should take the same name as the json file, but change the file extension to ".csv"
    csv_filepath = base_path+"/"+ str.split(filename, ".")[0]+".csv"

    # Convert the dataframe to a csv file in the specified directory
    df.to_csv(csv_filepath)

    return f"The csv File is stored at {csv_filepath}"



def main(base_path = r"C:\Users\K84277516.CHINA\Documents\KAINE DATA PROJECTS\rent_boss_parody\data"):


    # Find all json files in the data folder
    for file in os.listdir(base_path):
        if file.endswith(".json"):
            # Generate a csv file from the information in the json file
             json_to_csv(file, base_path)
