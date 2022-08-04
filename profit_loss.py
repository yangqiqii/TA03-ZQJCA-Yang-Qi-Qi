# Import modules to run code
from pathlib import Path
import csv
import api

# Define the function profit_loss()
def profit_loss():
    # Documentation of the function profit_loss()
    """
    Function does not require parameter
    Function returns the day where the net profit is lower than the previous day and the value of the difference.
    """
    # File path for profit-and-loss-usd.csv file
    # Assign the file path to the variable "file_path"
    file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
    # Create an empty list to store net profit value for each day
    netprofit_list = []
    # Create an empty list to store the days
    days_list = []
    # Create an empty list to store the difference between net profit
    difference_list = []
    # Create an empty list to store the summary statements for net profit
    summary = []
    # Open profit-and-loss-usd.csv file for reading
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        # Use csv.reader() to read csv file
        # Assign csv.reader(file) to the variable "reader"
        reader = csv.reader(file)
        # Use next() to skip the header
        next(reader)
        # Access the sub-list in reader
        for datas in reader:
            # Append net profit values into netprofit_list
            netprofit_list.append(float(datas[4]))
            # Append days into days_list
            days_list.append(datas[0])
        # Create "index" to represent the index postion of the items in netprofit_list
        # Create "index" to represent the index postion of the items in days_list
        index = 1
        # Use while loops to repeat appending summary statement into "summary" for index postion lesser than the number of items in netprofit_list
        while index < len(netprofit_list):
            # Use try to start exception handling
            try: 
                # Calculate the difference between net profit of the day and net profit of the day before it
                difference = (netprofit_list[index]) - (netprofit_list[index- 1])
            # Use except to handle TypeError
            except TypeError:
                # Return "There is a TypeError!" 
                return "There is a TypeError!"
            # Execute the followings if there is no TypeError
            else:
                # Append the differences into difference_list 
                difference_list.append(difference)
                # Use .sort() to sort the differences in ascending order
                difference_list.sort()
                # Increase the index postion by 1
                index += 1
                # Create a condition when the difference is less than or equals to 0
                if difference <= 0:
                    # Append summary statement into "summary" if the difference satisfy the above condition
                    # Use abs() to return the absolute value of difference
                    # Multiply difference with currency exchange rate to convert USD to SGD
                    # Use round( ,2) to round the value to 2 decimal places
                    summary.append(f"[PROFIT DEFICIT] DAY: {days_list[index - 1]}, AMOUNT: SGD{round(abs(difference * api.forex), 2)}")
                # Create a condition when the difference is more than 0
                else: 
                    # Skip iteration if the difference satisfy the above condition
                    continue
        # Create a condition when the 1st item of difference_list is more than 0
        if difference_list[0] > 0:
            # Append summary statement into "summary" if the 1st item of difference_list satisfy the above condition
            summary.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        # Return "summary"
        return summary
# Execute the function
print(profit_loss())