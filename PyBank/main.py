# import modules
import os
import csv

# set file path for csv file
csvpath = os.path.join("..","Resources",election_data.csv)

# declare variables
monthCount = 0
netProfit = 0
monthlyProfitChanges = []
months = []

# open csv file
with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    # skip header
    next(reader,None)

    # loop throough each row in csv file
    for row in csvreader

        # count the months
        monthCount = monthCount + 1

        # keep a running total of the profits. Profit is the second column (index 1)
        netProfit = netProfit + row[1]

        # if this is the first month, capture th profit in the first month as a reference for the change in profit for the next month
        if row == 1:

            lastMonthProfit = row[1]
        
        # after the first month, calculate the monthly change in profit, capture the month, and apend them to their rerspective lists.
        else:
            
            # add change in profit to list
            monthlyProfitChanges.append(row[1]-lastMonthProfit)

            # add month to list
            months.append(row[0])

            # set last month profit to the next value
            lastMonthProfit = row[1]

# define function to average the monthly profit change
def average(monthlyProfitChanges)

    # add all the monthly profit changes together
    totalChange = sum(monthlyProfitChanges)

    # get the number of records (the length of the list)
    countChange = len(monthlyProfitChanges)

    averageChange = totalChange/countChange

    return averageChange




