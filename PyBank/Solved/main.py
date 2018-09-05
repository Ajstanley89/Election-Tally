# import modules
import os
import csv

# set file path for csv file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# declare variables
monthCount = 0
netProfit = 0
monthlyProfitChanges = []
months = []
firstRow = True

# open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header
    next(csvreader,None)

    # loop throough each row in csv file
    for row in csvreader:

        # count the months
        monthCount = monthCount + 1

        # keep a running total of the profits. Profit is the second column (index 1)
        netProfit = int(netProfit) + int(row[1])

        # if this is the first month, capture th profit in the first month as a reference for the change in profit for the next month
        if firstRow == True:

            lastMonthProfit = int(row[1])

            firstRow = False
        
        # after the first month, calculate the monthly change in profit, capture the month, and apend them to their rerspective lists.
        else:
            
            profitChange = int(row[1]) - int(lastMonthProfit)

            # add change in profit to list
            monthlyProfitChanges.append(profitChange)

            # add month to list
            months.append(row[0])

            # set last month profit to the next value
            lastMonthProfit = row[1]

# define function to average the monthly profit change from a list as an iint
def average(monthlyProfitChanges):

    # add all the monthly profit changes together
    totalChange = sum(monthlyProfitChanges)

    # get the number of records (the length of the list)
    countChange = len(monthlyProfitChanges)

    average = totalChange/countChange

    return float(average)

# find average change in profits
averageProfitChange = average(monthlyProfitChanges)

# find max & max index
maxProfitChange = max(monthlyProfitChanges)
maxIndex = monthlyProfitChanges.index(maxProfitChange)

# find date of max
maxChangeDate = months[maxIndex]

# find min & min index
minProfitChange = min(monthlyProfitChanges)
minIndex = monthlyProfitChanges.index(minProfitChange)

#find date of min
minChangeDate = months[minIndex]

# can try zipping dates and profit change together
    # date_change = list(zip(months, monthlyProfitChanges))

    # print(f"{date_change[minIndex]}")

# specify output path
output_path = os.path.join("output", "py_bankresults.txt")

results_file = open(output_path, 'w')

def print_file(text):
    print(f"{text}")
    print(f"{text}", file=results_file)
    return

# print results header
print_file("Financial Analysis")
print_file("----------------------------")

# print results
print_file("Total Months: " + str(monthCount)) 
print_file("Total: $" + str(format(netProfit,",.2f")))
print_file("Average Change: $" + str(format(averageProfitChange,",.2f")))
print_file("Greatest Increase in Profits: " + str(maxChangeDate) + " ($" +  str(format(maxProfitChange,",.2f"))+")")
print_file("Greatest Decrease in Profits: " + str(minChangeDate) + " ($" + str(format(minProfitChange, ",.2f"))+")")





