import os
import csv

# Define file paths
# Get the absolute path to the election_data.csv file within the 'resources' directory
election_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "election_data.csv")

poll_candidate_and_votes = {}
# Read the CSV file
with open(election_data_path, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    for row in csv_reader:
        if row["Candidate"] not in poll_candidate_and_votes:
            poll_candidate_and_votes[row["Candidate"]] = 1
        else:
            poll_candidate_and_votes[row["Candidate"]] += 1


print(poll_candidate_and_votes)
    


