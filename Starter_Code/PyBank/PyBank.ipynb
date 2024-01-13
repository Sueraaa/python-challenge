{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a166fd07-8bd9-4eff-b1ed-9de9e6093f0f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "--------------------------\n",
      "Total no of Months: 86\n",
      "Net total amount: 22564198.0\n",
      "Average Change: -8311.11\n",
      "Greatest Increase in Profits: Aug-16 ($1862002.0)\n",
      "Greatest Decrease in Profits: Feb-14 ($-1825558.0)\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "\n",
    "# Define the function\n",
    "def analyse_records(file_path):\n",
    "    count = 0\n",
    "    total = 0\n",
    "    previous_profit_loss = 0\n",
    "    monthly_changes = []\n",
    "    months = []\n",
    "    \n",
    "    # Read in the CSV file\n",
    "    with open(file_path, 'r') as csv_file:\n",
    "        \n",
    "        # Split the data on commas\n",
    "        csv_reader = csv.reader(csv_file, delimiter=',')\n",
    "        \n",
    "        # Skip the header row\n",
    "        header = next(csv_reader)  \n",
    "        \n",
    "        # Loop through the data\n",
    "        for row in csv_reader:\n",
    "            \n",
    "            # Split the line into Date and Profit/Losses\n",
    "            date = row[0]\n",
    "            profit_loss = float(row[1])\n",
    "            \n",
    "            #Increment the count of months and accumulate the profit or loss of the current month\n",
    "            count += 1\n",
    "            total += profit_loss\n",
    "                \n",
    "            # Calculate the change in profit/loss\n",
    "            monthly_change = profit_loss - previous_profit_loss\n",
    "            monthly_changes.append(monthly_change)\n",
    "            months.append(date)\n",
    "\n",
    "            # Update previous profit/loss for the next iteration\n",
    "            previous_profit_loss = profit_loss\n",
    "     \n",
    "    # Calculate average change, exclude the first month from average calculation\n",
    "    average_change = sum(monthly_changes[1:]) / (count - 1)\n",
    "    \n",
    "    # Calculate the greatest increase in profits\n",
    "    greatest_increase = max(monthly_changes)\n",
    "    greatest_increase_index = monthly_changes.index(greatest_increase)\n",
    "    greatest_increase_date = months[greatest_increase_index]\n",
    "    \n",
    "    # Calculate the greatest decrease in profits\n",
    "    greatest_decrease = min(monthly_changes)\n",
    "    greatest_decrease_index = monthly_changes.index(greatest_decrease)\n",
    "    greatest_decrease_date = months[greatest_decrease_index]\n",
    "    \n",
    "    # Print the final data\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"--------------------------\")\n",
    "    print(f\"Total no of Months: {count}\")\n",
    "    print(f\"Net total amount: {total}\")\n",
    "    print(f\"Average Change: {average_change:.2f}\")\n",
    "    print(f\"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\")\n",
    "    print(f\"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\")\n",
    "\n",
    "# Path to collect data from the Resources folder\n",
    "csv_file = os.path.join('Resources', 'budget_data.csv')\n",
    "\n",
    "# Call the function\n",
    "analyse_records(csv_file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a58d5ee6-321a-4c58-9039-5470096ff2c9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
