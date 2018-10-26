import os
import csv


budget_data = '/Users/HarpreetSingh/Desktop/Python-Challenge/budget_data.csv'


with open(budget_data, 'r') as budget_data:
    
    csvreader = csv.reader(budget_data, delimiter=',')
    
    header = next(csvreader)
    
    profits = 0
    months = 0
    avgchng = []
    # Loop through the data
    for i, col in csvreader:
        profits += int(col[1])
        months += 1
        avgchng =

    print("Financial Analysis\n------------------")
    print(f"Total Months: {months}")
    print(f"Net Profit/Loss: ${profits}")


