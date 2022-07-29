from pathlib import Path
import csv
import api
def cash_on_hand():
    """
    Function does not require parameter
    Function returns the day where the cash on hand is lower than the previous day and the value of the difference.
    """
    file_path = Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
    cashonhand_list = []
    days_list = []
    difference_list = []
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        reader = csv.reader(file)
        next(reader)
        for datas in reader:
            cashonhand_list.append(float(datas[1]))
            days_list.append(datas[0])
    index = 1
    while index < len(cashonhand_list):
        difference = (cashonhand_list[index]) - (cashonhand_list[index - 1]) 
        difference_list.append(difference)
        difference_list.sort()
        index += 1
        if difference <= 0:
            deficit = f"[CASH DEFICIT] DAY: {days_list[index -1]}, AMOUNT: SGD{abs(difference * api.api())}"
        else:
            continue
        print(deficit)
    if difference_list[0] > 0:
        surplus = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        print(surplus)
print(cash_on_hand())