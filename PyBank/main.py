import os
import csv


budget_data = '/Users/HarpreetSingh/Desktop/Python-Challenge/budget_data.csv'


with open(budget_data, newline="") as data:
   csvreader = csv.reader(data, delimiter=",")


   next(csvreader)


   monthavg = []
   profits = []
   months = []
   avgchange = []


   for col in csvreader:

       months.append((col[0]))
       profits.append(int(col[1]))


   print("Total Months:", len(months))
   print("Total Profits:", sum(profits))

   # i: 3
   for i in range(2,len(profits)):
       monthavg.append(profits[i] - profits[i-1])
       avgchange = sum(monthavg)/len(profits)

       max_profit = max(profits)
       min_profit = min(profits)



   print("Average Profits per Month: $", avgchange)
   print("Best Profit: $", max_profit)
   print("Worst Profit: $", min_profit)


