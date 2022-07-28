from pathlib import Path
import csv
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
    print(cashonhand_list)
    index = 1
    while index < len(cashonhand_list):
        difference = (cashonhand_list[index]) - (cashonhand_list[index- 1]) 
        difference_list.append(difference)
        difference_list.sort()
        if difference < 0:
            message = f"[CASH DEFICIT] DAY: {days_list[index]}, AMOUNT: USD{abs(difference)}"
        else:
            message = ""
        print(message)
        index += 1
    if difference_list[0] > 0:
        message = "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    print(message)
print(cash_on_hand())