import os
import csv
import numpy as np

# set file paths
budget_data = os.path.join('Resources', 'budget_data.csv')
results_file_path = os.path.join('analysis', 'results.txt')

a = 0
months = {}
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")
    for row in csvreader:
        months[row[0]] = int(row[1])

# calculate totals
total_months = len(months)
total_amount = sum(months.values())
total_amount_formatted = '${:,.0f}'.format(total_amount)
average = total_amount / total_months
profit_month = max(months, key=months.get)
profit_value = months[profit_month]
loss_month = min(months, key=months.get)
loss_value = months[loss_month]

# write results to terminal
print('\n')
print('Financial Analysis')
print('-----------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {total_amount}')
print(f'Average Change: {average}')
print(f'Greatest Increase in Profits: {profit_month} (${profit_value})')
print(f'Greatest Decrease in Profits: {loss_month} (${loss_value})')
print('\n')

# write results to file
with open(results_file_path, 'w') as results:
    results.write('Financial Analysis\n')
    results.write('-----------------------------------\n')
    results.write('Total Months: {total_months}')
    results.write('Total: {total_amount}')
    results.write('Average Change: ' + '\n')
    results.write('Greatest Increase in Profits: ' + '\n')
    results.write('Greatest Decrease in Profits: ' + '\n')
    results.write('\n')

