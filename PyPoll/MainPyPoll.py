import os
import csv

file = os.path.join("election_data.csv")

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    Candidate = {}
    PercentVote = {}
    TotalVotes = 0
    MaxVotes = 0

    for row in csvreader:
        
        TotalVotes = TotalVotes + 1

        if row[2] not in Candidate:
            Candidate[row[2]] = 1
                
        else:
            Candidate[row[2]] = Candidate[row[2]] + 1
    
    for candidate, votes in Candidate.items():
        PercentVote[candidate] = ((votes/TotalVotes) * 100)

    for candidate in Candidate.keys():
        if Candidate[candidate] > MaxVotes:
            Winner = candidate
            MaxVotes = Candidate[candidate]

print("Election Results")    
print("------------------------")
print(f"Total Votes: {TotalVotes}")
print("------------------------")
for candidate, votes in Candidate.items():
    print(f"{candidate} : {PercentVote[candidate]}% ({votes})")
print("------------------------")
print(f"Winner: {Winner}")

Output = open("Output/output.txt", "w")

Output.write("Election Results \n")
Output.write("------------------------ \n")
Output.write(f"Total Votes: {TotalVotes} \n")
Output.write("------------------------ \n")
for candidate, votes in Candidate.items():
    Output.write(f"{candidate} : {PercentVote[candidate]}% ({votes}) \n")
Output.write("------------------------ \n")
Output.write(f"Winner: {Winner} \n")
