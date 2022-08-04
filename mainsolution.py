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
    # Open summary_report.txt file for appending
    cohsummary = cash_on_hand.cash_on_hand()
    plsummary = profit_loss.profit_loss()
    with summary_file.open(mode = "w", encoding = "UTF-8") as file:
        file.writelines(api.api())
    with summary_file.open(mode = "a", encoding = "UTF-8") as file:
        file.writelines(f" \n{overheads.overheads()}")
        while cohindex < len(cohsummary):
            file.writelines(f" \n{cohsummary[cohindex]}")
            cohindex +=1
        while plindex < len(plsummary):
            file.writelines(f"\n{plsummary[plindex]}")
            plindex += 1
mainSolution()
