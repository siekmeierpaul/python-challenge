import os
import csv

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
        a = a + 1
        # print(row)
    print(a)
    print(len(months))
    print(months.values())
    print(sum(months.values()))

# write results to terminal
print('\n')
print('Financial Analysis')
print('-----------------------------------')
print(f'Total Months: ' + '')
print(f'Total: ' + '')
print(f'Average Change: ' + '')
print(f'Greatest Increase in Profits: ' + '')
print(f'Greatest Decrease in Profits: ' + '')
print('\n')

# write results to file
with open(results_file_path, 'w') as results:
    results.write('Financial Analysis\n')
    results.write('-----------------------------------\n')
    results.write('Total Months: ' + '\n')
    results.write('Total: ' + '\n')
    results.write('Average Change: ' + '\n')
    results.write('Greatest Increase in Profits: ' + '\n')
    results.write('Greatest Decrease in Profits: ' + '\n')
    results.write('\n')

