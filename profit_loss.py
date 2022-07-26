from pathlib import Path
import csv
def profit_loss():
    """
    Function does not require parameter
    Function returns the day where the net profit is lower than the previous day and the value of the difference.
    """
    read_profitloss = []
    profit_loss = Path.cwd()/"csv_reports"/"profit-and-loss-hkd.csv"
    with profit_loss.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        for read_profitloss_lists in reader:
            read_profitloss.append(read_profitloss_lists)
        day40 = float(read_profitloss[1][4])
        day41 = float(read_profitloss[2][4])
        day42 = float(read_profitloss[3][4])
        day43 = float(read_profitloss[4][4])
        day44 = float(read_profitloss[5][4])
        day45 = float(read_profitloss[6][4])
        difference_dict = {
            41 : day41 - day40,
            42 : day42 - day41,
            43 : day43 - day42,
            44 : day44 - day43,
            45 : day45 - day44
            }
        for days in difference_dict:
            if difference_dict[days] > 0:
                return f"Day {days}'s net profit is lower than Day {days - 1}'s net profit by ${difference_dict[days]}."
print(profit_loss())