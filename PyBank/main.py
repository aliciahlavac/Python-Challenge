# Import necessary modules
import os
import csv

# Define variables used
MonthList = []
Difference = []
ChangeProfitLosses = 0
TotalMonth = 0
TotalRevenue = 0
CurrentProfitLosses = 0
PreviousProfitLosses = 0

# Set path to CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvpath) as csvfile:

    # Specify the delimiter and the CSV file to read in
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Read in the header row located in the first row of the Excel file
    csv_header = next(csvreader)

    # Loop through all data and get the total month count
    for row in csvreader:
        TotalMonth += 1

        # Get total Revenue count by grabbing the current month's profit/losses
        CurrentProfitLosses = int(row[1])
        TotalRevenue += CurrentProfitLosses

        # For the first month
        if(TotalMonth == 1):
            
            # Set previous month's profit/loss to current month's profit/loss
            PreviousProfitLosses = CurrentProfitLosses
        
        # If any other month other than the first month
        else:
            # Compute the difference in the profit/loss from one month to the other
            ChangeProfitLosses = CurrentProfitLosses - PreviousProfitLosses

            # Append the month onto the month list
            MonthList.append(row[0])

            # Append differences in profit/losses into differences list
            Difference.append(ChangeProfitLosses)

            # Reset the current profit/loss tracker to be the previous month's profit/loss
            PreviousProfitLosses = CurrentProfitLosses

# Sum the changes in Difference list
SumProfitLoss = sum(Difference)

# Calculate the average profit or loss and round the number to 2 decimal places
AverageProfitLoss = SumProfitLoss/len(Difference)
AverageProfitLoss = round(AverageProfitLoss,2)

# Find the highest and lowest changes in the difference list to find max/min profit/loss
HighestIncrease = max(Difference)
HighestDecrease = min(Difference)

# Find the best and worst month assosciated with these differences
HighestMonthLocator = Difference.index(HighestIncrease)
LowestMonthLocator = Difference.index(HighestDecrease)

# Actually find the month associated with the highest and lowest amount
HighestMonth = MonthList[HighestMonthLocator]
LowestMonth = MonthList[LowestMonthLocator]

# Print to terminal
print("\nFinancial Analysis\n")
print("---------------------------------------------\n")
print(f"Total Months: {TotalMonth}\n")
print(f"Total: ${TotalRevenue}\n")
print(f"Average Change: ${AverageProfitLoss}\n")
print(f"Greatest Increase in Profits: {HighestMonth} (${HighestIncrease})\n")
print(f"Greatest Decrease in Profits: {LowestMonth} (${HighestDecrease})\n")

# Write to Analysis.csv
output_path = os.path.join("Analysis", "analysis.txt")
with open(output_path, 'w') as outfile:
    outfile.write(f"\nFinancial Analysis\n")
    outfile.write(f"---------------------------------------------\n")
    outfile.write(f"Total Months: {TotalMonth}\n")
    outfile.write(f"Total: ${TotalRevenue}\n")
    outfile.write(f"Average Change: ${AverageProfitLoss}\n")
    outfile.write(f"Greatest Increase in Profits: {HighestMonth} ${HighestIncrease}\n")
    outfile.write(f"Greatest Decrease in Profits: {LowestMonth} ${HighestDecrease}\n")