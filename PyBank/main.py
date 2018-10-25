import os
import csv


budget_data = '/Users/HarpreetSingh/Desktop/Python-Challenge/budget_data.csv'


def totals(col):
    tot_profits = int(col[1])
    tot_months = int(col[0])


with open(budget_data, 'r') as budget_data:
    
    csvreader1 = csv.reader(budget_data, delimiter=',')
    
    header = next(csvreader1)
    
    profits = 0
    months = 0

    # Loop through the data
    for col in csvreader1:
        profits += int(col[1])
    print(f"Net Profit/Loss: ${profits}")

    for col in csvreader1:
        months += col[0]
    print(f"Total Months: {months}")






