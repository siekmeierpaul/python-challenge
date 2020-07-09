import os
import csv

# set file paths
election_data = os.path.join('Resources', 'election_data.csv')
results_file_path = os.path.join('analysis', 'results.txt')

# read csv file into dictionary
votes = {}
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        votes[row[0]] = row[2]

# calculate some totals
total_votes = len(votes)
receiving_votes = set(votes.values())

# candidates with all their voters in a list
candidates = {}
for receiver_of_votes in receiving_votes:
    candidates[receiver_of_votes] = [voter for voter,cand in votes.items() if cand == receiver_of_votes]

# candidates with just total votes    
candidate_totals = {}
for candidate, list_of_voters in candidates.items():
    candidate_totals[candidate] = len(list_of_voters)
winner = max(candidate_totals, key=candidate_totals.get)

# write results to terminal
print('\n')
print('Election Results')
print('-----------------------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------------------')
for candidate, candidate_total in candidate_totals.items():
    average = '{:.3%}'.format(candidate_total / total_votes)
    print(f'{candidate}: {average} ({candidate_total})')
print('-----------------------------------')
print(f'Winner: {winner}')
print('-----------------------------------')
print('\n')

# write results to file
with open(results_file_path, 'w') as results:
    results.write('Election Results\n')
    results.write('-----------------------------------\n')
    results.write(f'Total Votes: {total_votes}\n')
    results.write('-----------------------------------\n')
    for candidate, candidate_total in candidate_totals.items():
        average = '{:.3%}'.format(candidate_total / total_votes)
        results.write(f'{candidate}: {average} ({candidate_total})\n')
    results.write('-----------------------------------\n')
    results.write(f'Winner: {winner}\n')
    results.write('-----------------------------------\n')
    results.write('\n')
