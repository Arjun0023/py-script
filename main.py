import json
import pandas as pd

def json_to_excel(json_file, output_file):
    try:
        # Load JSON data from file
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Convert nested JSON to DataFrame
        df = pd.json_normalize(data)
        
        # Write DataFrame to Excel
        df.to_excel(output_file, index=False)
        
        print("Conversion successful. Excel file saved as:", output_file)
    except FileNotFoundError:
        print("Error: JSON file not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
    except Exception as e:
        print("An error occurred:", str(e))

# Example usage:
# Specify the input JSON file and output Excel file paths
input_json_file = "input.json"
output_excel_file = "output.xlsx"

# Call the function with the input JSON file and output Excel file paths
json_to_excel(input_json_file, output_excel_file)
