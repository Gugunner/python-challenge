# TODO GET TOTAL NUMBER OF VOTES
# TODO GET LIST OF CANDIDATES
# TODO GET PERCENTAGE OF VOTES PER CANDIDATE
# TODO GET NUMBER OF VOTES PER CANDIDATE
# TODO GET WINNER OF ELECTION
import os
import csv
# declare all global variables
elections = { 'candidates': {} }
csvPath = os.path.join('Resources', 'election_data.csv')

votes = 0

def checkForExistingCandidate(name):
    if not name in elections['candidates']:
        elections['candidates'][name] = { 'voteShare': 0.0, 'votes': 0 }

def addVotesToCandidate(name):
    votes = elections['candidates'][name]['votes']
    elections['candidates'][name]['votes'] += 1

def addVoteShareOfCandidate(total):
    for name in elections['candidates']:
        votes = elections['candidates'][name]['votes']
        elections['candidates'][name]['voteShare'] = (votes/total) * 100

def checkWinnerCandidate():
    winnerName = ''
    winnerVotes = 0
    for name in elections['candidates']:
        if elections['candidates'][name]['votes'] > winnerVotes:
            winnerVotes = elections['candidates'][name]['votes']
            winnerName = name

    return winnerName

with open(csvPath) as csvFile:
    csvreader = csv.reader(csvFile, delimiter = ',')
    # advance csv to skip header
    next(csvreader)
    # get enumerable list to get length of csv
    rows = [vote for vote in csvreader]
    votes = len(rows)
    for row in rows:
        # logic to add names and votes
        checkForExistingCandidate(row[2])
        addVotesToCandidate(row[2])
# after it's finished get percentage of each candidate
addVoteShareOfCandidate(votes)
# Create  all string variable before printing and writing to text file
results = [' Election Results', '------------------------', 
          f'Total Votes {votes}', '------------------------']

for name in elections['candidates']:
    votesShare = elections['candidates'][name]['voteShare']
    votes = elections['candidates'][name]['votes']
    results.append(f'{name}: ''%.3f'%votesShare+f'% ({votes})')

results.append('------------------------')
results.append(f'Winner: {checkWinnerCandidate()}')
results.append('------------------------')
# Printing and writing to file
for result in results:
    print(result)

analysis_file = os.path.join('analysis', 'analysis.txt')
analysis = open(analysis_file, 'w')
fileResults = [f'{result}\n 'for result in results ]
analysis.writelines(fileResults)