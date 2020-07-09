import os
import csv

# set file paths
budget_data = os.path.join('Resources', 'budget_data.csv')
results_file_path = os.path.join('analysis', 'results.txt')

# read csv file into dictionary
months = {}
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months[row[0]] = int(row[1])

# calculate difference in profit/loss for each month
month_by_month_differences = {}
first_month = True
for month, monthly_total in months.items():
    # need to skip first month because we do not know previous month's profit/loss
    if first_month:
        first_month = False
        last_month_total = monthly_total
        continue
    month_by_month_differences[month] = monthly_total - last_month_total
    last_month_total = monthly_total

# calculate totals
total_months = len(months)
total_amount = sum(months.values())
total_amount_formatted = '${:,.0f}'.format(total_amount)
monthly_change_total = sum(month_by_month_differences.values())
average = '${:,.2f}'.format(monthly_change_total / (total_months - 1))
profit_month = max(month_by_month_differences, key=months.get)
profit_value = '${:,.0f}'.format(month_by_month_differences[profit_month])
loss_month = min(month_by_month_differences, key=months.get)
loss_value = '${:,.0f}'.format(month_by_month_differences[loss_month])

# write results to terminal
print('\n')
print('Financial Analysis')
print('-----------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {total_amount_formatted}')
print(f'Average Change: {average}')
print(f'Greatest Increase in Profits: {profit_month} ({profit_value})')
print(f'Greatest Decrease in Profits: {loss_month} ({loss_value})')
print('\n')

# write results to file
with open(results_file_path, 'w') as results:
    results.write('Financial Analysis\n')
    results.write('-----------------------------------\n')
    results.write(f'Total Months: {total_months}\n')
    results.write(f'Total: {total_amount_formatted}\n')
    results.write(f'Average Change: {average}\n')
    results.write(f'Greatest Increase in Profits: {profit_month} ({profit_value})\n')
    results.write(f'Greatest Decrease in Profits: {loss_month} ({loss_value})\n')
    results.write('\n')

