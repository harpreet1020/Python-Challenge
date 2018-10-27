import os
import csv


budget_data = '/Users/HarpreetSingh/Desktop/Python-Challenge/budget_data.csv'


with open(budget_data, 'r') as budget_data:
    
    csvreader = csv.reader(budget_data, delimiter=',')
    # skip header in csv file
    next(csvreader)
    
    profits = 0
    months = 0
    change = [profits]
    rev_change = []
    # Loop through the data
    for col in csvreader:
        profits += int(col[1])
        months += 1
    for i in change:
        rev_change.append(change[i] - change[i - 1])
        avg_change = sum(rev_change) / len(rev_change)

    print("Financial Analysis\n------------------")
    print(f"Total Months: {months}")
    print(f"Net Profit/Loss: ${profits}")
    print(f"Average Change: {avg_change}")



