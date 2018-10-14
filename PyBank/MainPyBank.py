import os
import csv

file = os.path.join("budget_data.csv")

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    TotalMonths = 0
    TotalProfit = 0
    GreatestIncrease = 0
    GreatestDecrease = 0
    GreatestIncreaseDate = ""
    GreatestDecreaseDate = ""
    PL = []
    MonthlyDifference = []
    Month = []

    for row in csvreader:

        TotalMonths = TotalMonths + 1
        TotalProfit =  TotalProfit + int(row[1])
        
        PL.append(int(row[1]))

        Month.append(str(row[0]))

    MonthlyDifference = [(PL[i+1]) - (PL[i]) for i in range(len(PL)-1)]       
    DiffSum = sum(MonthlyDifference)
    AverageChange = DiffSum/((TotalMonths)-1)

    for i in range(len(MonthlyDifference)-1):
        
        if int(MonthlyDifference[i]) >= GreatestIncrease:
            GreatestIncrease = int(MonthlyDifference[i])
            GreatestIncreaseDate = Month[i+1]
    
        if int(MonthlyDifference[i]) <= GreatestDecrease:
            GreatestDecrease = int(MonthlyDifference[i])
            GreatestDecreaseDate = Month[i+1]

    

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(TotalMonths))
print("Total Profit: $" + str(TotalProfit))
print("Greatest Increase in Profits: " + GreatestIncreaseDate + " $" + str(GreatestIncrease))
print("Greatest Decrease in Profits: " + GreatestDecreaseDate + " $" + str(GreatestDecrease))
print("Average Change: $" + str(AverageChange))

Output = open("Output/output.txt", "w")

Output.write("Financial Analysis \n")
Output.write("------------------------- \n")
Output.write("Total Months: " + str(TotalMonths) + "\n")
Output.write("Total Profit: $" + str(TotalProfit) + "\n")
Output.write("Greatest Increase in Profits: " + GreatestIncreaseDate + " $" + str(GreatestIncrease) + "\n")
Output.write("Greatest Decrease in Profits: " + GreatestDecreaseDate + " $" + str(GreatestDecrease) + "\n")
Output.write("Average Change: $" + str(AverageChange) + "\n")