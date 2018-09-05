# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

  # The total number of votes cast
    #keep a running tally fro each row in csv file. Eeach row is 1 vote

  # A complete list of candidates who received votes
    # Put the "candidate" column in a list
    # use for loop/list comprehension to put each unique candidate into a new list (for each candidate in candidates)
        #if "candidate" not already in "unique candidate list", append that candidate to "unique candidate list"

  # The percentage of votes each candidate won
    # define function to calculate percdentage
    # percentage = candidate votes/total number of votes

  # The total number of votes each candidate won
    # need to calculate this before getting percentage

  # The winner of the election based on popular vote.
    # put total number of votes into a list or dictionary
    # find the max in that list

# import modules
import os
import csv

# set file path for csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# define candidate list
candidates = []

# define unique candidate list
unique_candidates = []

# define the dashes that separate everything in the heeader
separator = "-------------------------"

#open csv file
with open(csvpath, newline="") as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader,None)

    # fill the list of candidates
    for row in csvreader:
        candidates.append(row[2])

#non-list comprehension method
for candidate in candidates:
    if candidate not in unique_candidates:
        unique_candidates.append(candidate)

# get the number of candidates (the length of the set)
num_candidates = len(unique_candidates)

# get the total number of votes cast
total_votes = len(candidates)

# use list comprehension to create individual lists of each candidate's vote count, then get the length of that list to get the total number of votes
khan_count = len([candidate for candidate in candidates if candidate == "Khan"])
correy_count = len([candidate for candidate in candidates if candidate == "Correy"])
li_count = len([candidate for candidate in candidates if candidate == "Li"])
otooley_count = len([candidate for candidate in candidates if candidate == "O'Tooley"])

# Create a dictionary pairing the candidates name with their vote totals
all_votes = {"Khan":khan_count, "Correy":correy_count, "Li":li_count, "O'Tooley":otooley_count}

# find the maximum of votes from the dictoary and return the key of that value (the winner)
winner = max(all_votes, key=all_votes.get)

# specify output path
output_path = os.path.join("output", "results.txt")

results_file = open(output_path, 'w')

# define function to calculate the percentage of votes each candidate received, print it out, and write to file
def percentage(candidate, candidate_vote_dictionary, total):
    votes = candidate_vote_dictionary.get(candidate, "")
    vote_percent = 100*(int(votes)/total)
    print(f"{candidate}: {vote_percent:.2f}% ({candidate_vote_dictionary[candidate]})")
    print(f"{candidate}: {vote_percent:.2f}% ({candidate_vote_dictionary[candidate]})", file=results_file)
    # results_file.write(f"{candidate}: {vote_percent:.2f}% ({candidate_vote_dictionary[candidate]})")
    return

def print_file(text):
    print(f"{text}")
    print(f"{text}", file=results_file)
    return

# print header
print_file("Election Results")
print_file(separator)
# print total votes
print_file("Total Votes: " + str(total_votes))
print_file(separator)

# print individual results using defined function
for unique_candidate in unique_candidates:
    percentage(unique_candidate, all_votes, total_votes)

print_file(separator)

# Print winner, and make Star Trek joke if Khan wins
if winner == "Khan":
    print_file("The winner is: Khhhhhhhaaaaaaaaaaaaaannnnnnnnn!!!!!!!")
else:
    print_file("The winner is: " + str(winner))


   



