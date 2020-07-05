import os
import csv

bank_csv = os.path.join('Resources', 'election_data.csv')
a = 0
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")
    for row in csvreader:
        a = a + 1
        # print(row)
    print(a)
