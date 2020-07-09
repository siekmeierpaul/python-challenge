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

# calculate totals
total_votes = len(votes)
receiving_votes = set(votes.values())
candidates = {}
for receiver_of_votes in receiving_votes:
    candidates[receiver_of_votes] = [voter for voter,cand in votes.items() if cand == receiver_of_votes]
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
for candidate, voters in candidates.items():
    average = '{:.3%}'.format(len(voters) / total_votes)
    print(f'{candidate}: {average} ({len(voters)})')
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
    for candidate, voters in candidates.items():
        average = '{:.3%}'.format(len(voters) / total_votes)
        results.write(f'{candidate}: {average} ({len(voters)})\n')
    results.write('-----------------------------------\n')
    results.write(f'Winner: {winner}\n')
    results.write('-----------------------------------\n')
    results.write('\n')
