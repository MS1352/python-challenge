import os
import csv

# Define file paths
# Get the absolute path to the election_data.csv file within the 'resources' directory
election_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "election_data.csv")
poll_report_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "analysis", "poll_report.txt")


# Function to print poll results in the desired format and return the output as a multi-line string
def print_poll_results(candidate_votes, total_votes):
    output = "Election Results\n"
    output += "-------------------------\n"
    output += f"Total Votes: {total_votes}\n"
    output += "-------------------------\n"
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    output += "-------------------------\n"
    winner = max(candidate_votes, key=candidate_votes.get)
    output += f"Winner: {winner}\n"
    output += "-------------------------\n"
    
   
    print(output)   
    
    return output

# Function to export poll result report to a file
def export_to_file(poll_resut_report):
    with open(poll_report_path, 'w') as output_file:
        output_file.write(poll_resut_report)




poll_candidate_and_votes = {}
total_votes = 0
# Read the CSV file
with open(election_data_path, 'r') as file:
    #It reads and get rid of the header file, so the data doesn't have the header file in it
    csv_reader = csv.DictReader(file, delimiter=',')
    for row in csv_reader:
        total_votes+= 1
        if row["Candidate"] not in poll_candidate_and_votes:
            poll_candidate_and_votes[row["Candidate"]] = 1
        else:
            poll_candidate_and_votes[row["Candidate"]] += 1

poll_resut_report = print_poll_results(poll_candidate_and_votes, total_votes)

# Export the results to a text file
export_to_file(poll_resut_report)
    


