from pathlib import Path
import csv
import api
def profit_loss():
    """
    Function does not require parameter
    Function returns the day where the net profit is lower than the previous day and the value of the difference.
    """
    file_path = Path.cwd()/"csv_reports"/"profit-and-loss-usd.csv"
    netprofit_list = []
    days_list = []
    difference_list = []
    summary = []
    with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        reader = csv.reader(file)
        next(reader)
        for datas in reader:
            netprofit_list.append(float(datas[4]))
            days_list.append(datas[0])
        index = 1
        while index < len(netprofit_list):
            difference = (netprofit_list[index]) - (netprofit_list[index- 1]) 
            difference_list.append(difference)
            difference_list.sort()
            index += 1
            if difference <= 0:
                summary.append(f"[PROFIT DEFICIT] DAY: {days_list[index - 1]}, AMOUNT: SGD{round(abs(difference * api.forex), 2)}")
            else: 
                continue
        if difference_list[0] > 0:
            summary.append("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        return summary
print(profit_loss())