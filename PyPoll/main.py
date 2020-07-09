import os
import csv

# set file paths
election_data = os.path.join('Resources', 'election_data.csv')
results_file_path = os.path.join('analysis', 'results.txt')

a = 0
votes = {}
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")
    for row in csvreader:
        votes[row[0]] = row[2]
        a = a + 1
        # print(row)
    print(a)
    print(len(votes))
    receiving_votes = set(votes.values())
    candidates = {}
    for receiver_of_votes in receiving_votes:
        candidates[receiver_of_votes] = [voter for voter,cand in votes.items() if cand == receiver_of_votes]
    
    for candidate, voters in candidates.items():
        print(f"{candidate} has {len(voters)}")
    
# write results to terminal
print('\n')
print('Election Results')
print('-----------------------------------')
print('Total Votes: ' + '')
print('-----------------------------------')
print(':' + '')
print('-----------------------------------')
print('Winner: ' + '')
print('-----------------------------------')
print('\n')

# write results to file
with open(results_file_path, 'w') as results:
    results.write('Election Results\n')
    results.write('-----------------------------------\n')
    results.write('Total Votes: ' + '\n')
    results.write('-----------------------------------\n')
    results.write(':' + '\n')
    results.write('-----------------------------------\n')
    results.write('Winner: ' + '\n')
    results.write('-----------------------------------\n')
    results.write('\n')
