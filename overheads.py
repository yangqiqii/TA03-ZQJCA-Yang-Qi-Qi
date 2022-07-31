from pathlib import Path
import csv
def overheads():
    """
    Function does not require parameter
    Function returns the highest overhead category and its value.
    """
    dictionary = {}
    value_list = []
    overheads = Path.cwd()/"csv_reports"/"overheads-day-45.csv"
    with overheads.open(mode = "r", encoding = "UTF-8") as file:
        reader = csv.reader(file)
        next(reader)
        for datas in reader:
            categorydata = datas[0]
            valuedata = float(datas[1])
            dictionary[categorydata] = valuedata
            value_list.append(valuedata)
        for category, values in dictionary.items():
            if values == max(value_list):
                return f"[HIGHEST OVERHEADS] {category.upper()}: {max(value_list)}%"
print(overheads())