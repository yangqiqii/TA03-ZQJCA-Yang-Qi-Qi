from pathlib import Path
import csv
# def coh():
file_path = Path.cwd()/"csv_reports"/"cash-on-hand-hkd.csv"
empty_list = []
empty_list2 = []

with file_path.open(mode = 'r', encoding = 'UTF-8', newline ='' ) as file:
        reader = csv.reader(file)
        next(reader)

        for line in reader:
                empty_list.append(line)

x = 0
for data in range (len(empty_list)):
                if x+1 >= len(empty_list):
                        exit
                else:
                        diff =  int(empty_list[x][1])- int(empty_list[x+1][1])
                        if diff <= 0:
                                print('CASH DEFICIT DAY:',empty_list[x][0],'AMOUNT:USD',empty_list[x][1])
                        x = x + 1
