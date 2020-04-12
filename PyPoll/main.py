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

totalVotes = 0

def checkForExistingCandidate(candidate):
    if not candidate in elections['candidates']:
        elections['candidates'][candidate] = { 'voteShare': 0.0, 'votes': 0 }

def addVotesToCandidate(candidate):
    votes = elections['candidates'][candidate]['votes']
    elections['candidates'][candidate]['votes'] += 1

def addVoteShareOfCandidate(candidate):
    global totalVotes
    votes = elections['candidates'][candidate]['votes']
    elections['candidates'][candidate]['voteShare'] = (votes/totalVotes) * 100

def checkWinnerCandidate():
    winnerName = ''
    winnerVotes = 0
    for candidate in elections['candidates']:
        if elections['candidates'][candidate]['votes'] > winnerVotes:
            winnerVotes = elections['candidates'][candidate]['votes']
            winnerName = candidate

    return winnerName

with open(csvPath) as csvFile:
    csvreader = csv.reader(csvFile, delimiter = ',')
    
    # advance csv to skip header
    next(csvreader)

    # get enumerable list to get length of csv
    rows = [vote for vote in csvreader]
    totalVotes = len(rows)

    # Used tupples for each csv column
    for (voterId, county, candidate) in rows:
        # logic to add names and votes
        checkForExistingCandidate(candidate)
        addVotesToCandidate(candidate)

# after it's finished get percentage of each candidate with a list comprehension
[addVoteShareOfCandidate(candidate) for candidate in elections['candidates']]

# Create  all string variable before printing and writing to text file
results = [' Election Results', '------------------------', 
          f'Total Votes {totalVotes}', '------------------------']

for candidate in elections['candidates']:
    votesShare = elections['candidates'][candidate]['voteShare']
    votes = elections['candidates'][candidate]['votes']
    results.append(f'{candidate}: ''%.3f'%votesShare+f'% ({votes})')

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