# Import necessary modules
import os
import csv

# Set the necessary variables
TotalVotes = 0
# Create a dictionary to hold the candidates and the number of votes they receive 
CandidatesVotes = {}
Candidates = []
Votes = []
VotesPercent = []
WinnerVotes = 0

# Set path to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Specify the delimiter and the CSV file to read in
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read in the header row located in the first row of the Excel file 
    csv_header = next(csvreader)

    #  Loop through all data and get total number of votes cast
    for row in csvreader:
        # Increment total number of votes casted
        TotalVotes += 1
        # Check to see if candidate's name is in dictionary already to avoid duplicates
        if row[2] in CandidatesVotes.keys():
            # Increment the vote counter for the candidate
            CandidatesVotes[row[2]] += 1
        else:
            # Start counting candidate's vote if not in dictionary
            CandidatesVotes[row[2]] = 1

# Place all votes into a dictionary (one for the candidate name and one for the vote count)
#I utilized the following source to learn how to iterate through a dictionary:
# “How to Iterate through a Dictionary in Python.” Real Python, 1 Apr. 2023, realpython.com/iterate-through-dictionary-python/#iterating-
# through-items. 
for key, value in CandidatesVotes.items():
    # Append the key (candidates) to the candidates list
    Candidates.append(key)
    # Append the value (total number of votes) to the votes list
    Votes.append(value)

# Calculate the percentage won by each candidate:
for Vote in Votes:
    VotesPercent.append(round(Vote/(sum(Votes))*100,3))

# Zip all the data together (candidate name, total number of votes, and percent of votes won), and set as a list
Complete = list(zip(Candidates, Votes, VotesPercent))

# Run through a for loop of each candidate, their total votes, and the percentage of votes won to find the winner
for Candidate in Complete:
    # Compare candidate's number of votes with the maximum number of votes in the votes list to pick the winning candidate
    if Candidate[1] == max(Votes):
        # Get the winning candidate's name from the candidate selection
        Winner = Candidate[0]

#Print to terminal
print(f"\nElection Results\n")
print(f"-----------------------------------------\n")
print(f"Total Votes: {TotalVotes}\n")
print(f"-----------------------------------------\n")
# Create a for loop to print out candidate information
for name in Complete:  
    print(f"{name[0]}: {name[2]}% ({name[1]})\n")
print(f"-----------------------------------------\n")
print(f"Winner: {Winner}\n")
print(f"-----------------------------------------\n")

#Write to Analysis.csv
output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, 'w') as outfile:
    outfile.write(f"Election Results\n")
    outfile.write(f"-----------------------------------------\n")
    outfile.write(f"Total Votes: {TotalVotes}\n")
    outfile.write(f"-----------------------------------------\n")
    # Create a for loop to print out candidate information
    for name in Complete:  
        outfile.write(f"{name[0]}: {name[2]}% ({name[1]})\n")
    outfile.write(f"-----------------------------------------\n")
    outfile.write(f"Winner: {Winner}\n")  
    outfile.write(f"-----------------------------------------\n")
