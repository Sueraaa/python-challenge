import os
import csv

# Path to collect data from the Resources folder
csv_file_path = os.path.join('Resources', 'election_data.csv')

# Define the function
def calculate_values(file_path):
    total_votes = 0
    candidates_votes = {}

    # Read in the CSV file
    with open(file_path, 'r') as csv_file:
        
        # Split the data on commas
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        # Skip the header row
        header = next(csv_reader)
        
        # Loop through the data
        for row in csv_reader:
            
            # Split the line into Ballot_ID, County, and Candidate
            ballot_id = row[0]
            county = str(row[1])
            candidate= str(row[2])
            
            
            # Increment the total_votes
            total_votes += 1
            # increments the vote count for a particular candidate
            candidates_votes[candidate] = candidates_votes.get(candidate, 0) + 1
    
     #print results
    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------")
    
    # Iterate through the candidates_votes dictionary
    for candidate, votes in candidates_votes.items():
    # Calculate the percentage of votes for the current candidate
        percentage = (votes / total_votes) * 100
         #print the result with the votes count
        print(f"{candidate}: {percentage:.2f}% ({votes} votes)")
        
    # Determine the winner based on popular vote
    winner = max(candidates_votes, key = candidates_votes.get)
    print("------------------")
    print(f"Winner: {winner}")
    print("------------------")


#Call the function
calculate_values(csv_file_path)

