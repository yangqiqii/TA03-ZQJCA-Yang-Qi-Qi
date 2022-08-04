# Import modules to run code
from pathlib import Path
import api, overheads, cash_on_hand, profit_loss

# Define the function mainSolution()
def mainSolution():
    # Documentation of the function mainSolution()
    """
    Function does not require parameter
    Function returns summary report for currency exchange rate, overheads, cash on hand and profit and loss
    """
    # File path for summary_report.txt_file
    # Assign the file path to the variable "summary_file"
    summary_file = Path.cwd()/"summary_report.txt"
    # Use .touch() to creatae the summary_report.txt file
    summary_file.touch()
    # Create "cohinder" to represent the index position of the items in the output  of cash_on_hand.cash_on_hand()
    cohindex = 0
    # Create "plindex" to represent the index position of the items in the output of the profit_loss.profit_loss()
    plindex = 0
    # Open summary_report.txt file for writing
    with summary_file.open(mode = "w", encoding = "UTF-8") as file:
        file.writelines(api.api())
    # Open summary_report.txt file for appending
    with summary_file.open(mode = "a", encoding = "UTF-8") as file:
        # Use .writelines() to write the output of overheads.overheads() into summary_report.txt file
        # Use \n to add the item into a new line
        file.writelines(f" \n{overheads.overheads()}")
        # Creating a while loop to repeat appending summary statement into summary_report.txt file for cohindex lesser than the number of items in the output of cash_on_hand.cash_on_hand()
        while cohindex < len(cash_on_hand.cash_on_hand()):
            # Use .writeline() to write the output of cash_on_hand.cash_on_hand() into summary_report.txt file
            # Use \n to add the items into a new line
            file.writelines(f" \n{cash_on_hand.cash_on_hand()[cohindex]}")
            # To increase index position by 1
            cohindex +=1
            
        # Creating while loop to repeat appending summary statement into summary_report.txt file fot plindex lesser than the number of  items in the output of profit_loss.profit_loss()
        while plindex < len(profit_loss.profit_loss()):
            # Use .writeline() to write the output of profit_loss.profit_loss() into summary_report.txt file
            # Use \n to add the items into a new line
            file.writelines(f"\n{profit_loss.profit_loss()[plindex]}")
            # To increase index position by 1
            plindex += 1
# To exceute the function
mainSolution()
