import os
import csv

# Define the function
def analyse_records(file_path):
    count = 0
    total = 0
    previous_profit_loss = 0
    monthly_changes = []
    months = []
    
    # Read in the CSV file
    with open(file_path, 'r') as csv_file:
        
        # Split the data on commas
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        # Skip the header row
        header = next(csv_reader)
        
        # Loop through the data
        for row in csv_reader:
            
            # Split the line into Date and Profit/Losses
            date = row[0]
            profit_loss = float(row[1])
            
            #Increment the count of months and accumulate the profit or loss of the current month
            count += 1
            total += profit_loss
                
            # Calculate the change in profit/loss
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)
            months.append(date)

            # Update previous profit/loss for the next iteration
            previous_profit_loss = profit_loss
     
    # Calculate average change, exclude the first month from average calculation
    average_change = sum(monthly_changes[1:]) / (count - 1)
    
    # Calculate the greatest increase in profits
    greatest_increase = max(monthly_changes)
    greatest_increase_index = monthly_changes.index(greatest_increase)
    greatest_increase_date = months[greatest_increase_index]
    
    # Calculate the greatest decrease in profits
    greatest_decrease = min(monthly_changes)
    greatest_decrease_index = monthly_changes.index(greatest_decrease)
    greatest_decrease_date = months[greatest_decrease_index]
    
    # Print the final data
    print("Financial Analysis")
    print("--------------------------")
    print(f"Total no of Months: {count}")
    print(f"Net total amount: {total}")
    print(f"Average Change: {average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Path to collect data from the Resources folder
csv_file = os.path.join('Resources', 'budget_data.csv')

# Call the function
analyse_records(csv_file)
