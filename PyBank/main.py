import os
import csv

# Define file paths
# Get the absolute path to the budget_data.csv file within the 'resources' directory
budget_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "budget_data.csv")
# Define the path for the financial analysis report file
analysis_report_path = "financial_analysis.txt"

# Function to calculate financial metrics
def calculate_metrics(data):
    total_months = 0
    net_total = 0
    previous_profit_loss = 0
    changes = []
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    # Iterate through each row of data
    for row in data:
        # Count total months
        total_months += 1
        # Calculate net total amount
        net_total += int(row['Profit/Losses'])
        profit_loss = int(row['Profit/Losses'])

        # Calculate change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = row['Date']
            elif change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = row['Date']

        previous_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes) if changes else 0

    # Generate financial analysis report
    analysis_results = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
        f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})"
    )

    return analysis_results

# Function to print financial analysis report
def print_results(analysis_results):
    print(analysis_results)
    return analysis_results

# Function to export financial analysis report to a file
def export_to_file(analysis_results):
    with open(analysis_report_path, 'w') as output_file:
        output_file.write(analysis_results)

# Read the CSV file
with open(budget_data_path, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    data = list(csv_reader)

# Calculate metrics
analysis_results = calculate_metrics(data)

# Print the results and return them
analysis_results = print_results(analysis_results)

# Export the results to a text file
export_to_file(analysis_results)
