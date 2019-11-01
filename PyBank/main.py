# This code is designed to analyze our bank's reporting data 
#Step 1: Import dependencies
import os
import csv

#Next import the data
bank_data = os.path.join('..','budget_data.csv')

#set up starting variables
rowcount = 0
net_total = 0
greatest_in = 0
greatest_de = 0
last_pl = 0
change_sum = 0
with open(bank_data, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    #set up the for loop for retrieving the information
    for row in csvreader:
        #save the profit/loss value
        pl = float(row[1])

        #get the rowcount for our number of months
        rowcount += 1
        # sum of the profit/losses
        net_total += pl
        # find the change in profit/loss
        change = last_pl - pl
       #save the greatest increase in profits 
        if change > greatest_in :
            greatest_in = change
            great = str(row[0])
        #save the greatest decrease in profits
        if change < greatest_de :
            greatest_de = change
            worst = str(row[0])
        #increase the change sum
        change_sum += change
        #set the current value as the last value
        last_pl = pl



#Total number of months
print(rowcount)
#Total net profit/loss
print(net_total)
#Average change
print(change_sum/rowcount)
#Greatest Increase and the month it occured in
print(great + " " + str(greatest_in))
#greatest decrease and the month it occured in
print(worst + " " + str(greatest_de))

