# Import modules to run code
from pathlib import Path
import csv
import api

# Define the function overheads()
def overheads():
    # Documentation of the function overheads()
    """
    Function does not require parameter
    Function returns the highest overhead category and its value.
    """
    # Create an empty dictionary to store catedory(key) : values(value)
    dictionary = {}
    # Create an empty list to store the values of each category
    value_list = []
    # File path for overheads-day-45.csv file
    # Assign the filepath to the variable "overheads"
    overheads = Path.cwd()/"csv_reports"/"overheads-day-45.csv"
    # Open overheads-day-45.csv for reading
    with overheads.open(mode = "r", encoding = "UTF-8") as file:
        # Use csv.reader() to to read csv file
        # Assign csv.reader (file) to the variable "reader"
        reader = csv.reader(file)
        # Using next() to skip the header
        next(reader)
        # Access the sub-list in reader
        for datas in reader:
            # Assign the 1st item of each sub-list as "categorydata"
            categorydata = datas[0]
            # Assign the 2nd item of each sub-list as "valuedata"
            # Use float() to convert the item from string to float
            valuedata = float(datas[1])
            # Add a key-value pair into "dictionary" with categorydata as the key and valuedata as the value
            dictionary[categorydata] = valuedata
            # Append "valuedata" into value_list
            value_list.append(valuedata)
        # Use .items() to return a tuple of key-value within a special type of list
        # caterogy(value) : values(value)
        for category, values in dictionary.items():
            # Use max() to find the highest value in value_list
            # Create a condition when values is the same as the highest value in value_list
            if values == max(value_list):
                # Return summary statement for overheads
                return f"[HIGHEST OVERHEADS] {category.upper()}: SGD{round(max(value_list)*api.forex, 2)}"
# Execute the function
print(overheads())
