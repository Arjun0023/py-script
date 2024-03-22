#Importing libraries

import json
import pandas as pd

#main function to Open JSON file , Loading JSON data , Convert JSON to DataFrame

def json_to_excel(json_file, output_file):
    try:
        with open(json_file, 'r') as f:
            data = json.load(f) #loads json data
        df = pd.json_normalize(data) #converts json data
        df.to_excel(output_file, index=False) #explore data & ensure  that the index of the DataFrame is not included in the Excel file.
        print("Conversion successful. Excel file saved as:", output_file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError: #Error handling.
        print("Error: Invalid JSON format.")
    except Exception as e:
        print("An error occurred:", str(e))

# Specify the input JSON file and output Excel file paths
input_json_file = "input.json"
output_excel_file = "output.xlsx"

# Calling the main function.
json_to_excel(input_json_file, output_excel_file)
