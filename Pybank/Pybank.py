import os
import csv
from pathlib import Path

# To get position of the file
input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'budget_data.csv')

# Create empty lists to iterate through specific rows for the following variables
total_months = []
total_profit = []
monthly_profit_change = []


with open(input_file) as csv_file:
    # csv reader reads delimiter and variable that holds data
    csv_reader = csv.reader(csv_file)

    # print(csvreader)
    # Skip the header/labels to iterate with the values
    next(csv_reader)
    # Iterate through the rows in the stored file contents
    for line in csv_reader: 
        # Append the total months total profit to their corresponding lists 
        print(line)
        total_months.append(line[0])
        total_profit.append(int(line[1]))


    print(len(total_months))

    # Iterate through the profits in the order to get the monthly change in profits 
    for i in range(len(total_profit) - 1):
        # Take the difference between two months and append to monthly profit change 
        monthly_profit_change.append(total_profit[i + 1] - total_profit[i])
    
    

# Obtain the max and min of the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
# We use the plus 1 at the end since month associated with change is the + 1 month or next month 
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

# Print Statements

print("Financial Analysis")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#Output files
output_file = Path("//Users//SRI//MonashBootcamp//Week//Python//PybankOutput.txt")

with open(output_file, "w") as file:
    # Write methods to print to Financial_Analysis_Summary
    file.write("Financial Analysis")
    file.write("\n")
    file.write("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
    file.write('\n')
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (S{(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest decrease in Profits: {total_months[max_decrease_month]} (S{(str(max_decrease_value))})")