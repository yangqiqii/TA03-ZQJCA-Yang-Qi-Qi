# Import modules to run code
from pathlib import Path
import csv
import api

# Define the function cash_on_hand()
def cash_on_hand():
    # Documentation of the function cash_on_hand()
    """
    Function does not require parameter
    Function returns the day where the cash on hand is lower than the previous day and the value of the difference.
    """
    # File path for cash-on-hand-usd.csv.file
    # Assign the file path to the variable "file_path"
    file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    # Create an empty list to store the cash on hand values for each day
    cashonhand_list = []
    # Create an empty list to store the days
    days_list = []
    # Create and empty list to store the differences between cash on hand
    difference_list = []
    # Create an empty list to store the summary statements for cash-on-hand
    summary = []
    # Open cash-on-hand-usd.csv file for reading 
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        # Use csv.reader() to read csv file
        # Assign csv.file(reader) to the variable "reader"
        reader = csv.reader(file)
        # Use next() to skip the header
        next(reader)
        # Access the sub-list in reader
        for datas in reader:
            # Append cash on hand values into cashonhand_list
            cashonhand_list.append(float(datas[1]))
            # Append days into days_list
            days_list.append(datas[0])
        # Create "index" to represent the index position of the items in the cashonhand_list
        # Create "index" to represent the index position of the items in the days_list
        index = 1
        # Use while loop to repeat appending summary statement into "summary" for index position lesser than the number of items in cashonhand_list
        while index < len(cashonhand_list):
            # Use try to start exception handling
            try:
                # Calculate the difference between cash on hand of the day and cash on hand of the day before it
                difference = (cashonhand_list[index]) - (cashonhand_list[index - 1]) 
            # Use except to handle TypeError
            except TypeError:
                # Return "There is a TypeError!"
                return "There is a TypeError!"
            # Execute the followings if there is no TypeError
            else:
                # Append the differences into difference_list
                difference_list.append(difference)
                #Use .sort() to sort the differences in ascending order
                difference_list.sort()
                # Increase the index position by 1
                index += 1
                # Create a condition when the difference is less than or equals to 0
                if difference <= 0:
                    # Append summary statement into "summary" if the difference satisfy the above condition
                    # Use abs() to returnthe absolute value of difference 
                    # Multiply difference with currency exchange rate to convert USD to SGD
                    # Use round( ,2) to round the values to 2 decimal places
                    summary.append(f"[CASH DEFICIT] DAY: {days_list[index -1]}, AMOUNT: SGD{round(abs(difference*api.forex), 2)}")
                # Create a condition when the difference is more than 0
                else:
                    # Skip iteration if the difference satisfy the above condition
                    continue  
        # Create a condition when the 1st item of difference_list is more than 0
        if difference_list[0] > 0:
            # Append summary statement into "summary" if the 1st item of difference_list satisfy the above condition
            summary.append("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # Return "summary"
        return summary
# Execute the function
print(cash_on_hand())
