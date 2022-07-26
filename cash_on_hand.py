from pathlib import Path
import csv
def cash_on_hand():
    """
    Function does not require parameter
    Function returns the day where the cash on hand is lower than the previous day and the value of the difference.
    """
    read_cashonhand = []
    cash_on_hand = Path.cwd()/"csv_reports"/"cash-on-hand-hkd.csv"
    with cash_on_hand.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        for read_cashonhand_lists in reader:
            read_cashonhand.append(read_cashonhand_lists)
        print(read_cashonhand)
        day40 = float(read_cashonhand[1][1])
        day41 = float(read_cashonhand[2][1])
        day42 = float(read_cashonhand[3][1])
        day43 = float(read_cashonhand[4][1])
        day44 = float(read_cashonhand[5][1])
        day45 = float(read_cashonhand[6][1])
        difference_dict = {
            41 : day41 - day40,
            42 : day42 - day41,
            43 : day43 - day42,
            44 : day44 - day43,
            45 : day45 - day44
            }
        for days in difference_dict:
            if difference_dict[days] < 0:
                return f"Day {days}'s cash on hand is lower than Day {days - 1}'s cash on hand by ${difference_dict[days]}."
print(cash_on_hand())