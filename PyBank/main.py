import os
import csv
csvpath = os.path.join(".","Resources","budget_data.csv")
month_count = 0
net_amount = 0

prev_val=0
greatest_increase = 0
greatest_decrease = 0

with open (csvpath, newline='') as budgetfile:

    csvread = csv.reader(budgetfile, delimiter=',')
    # skip  the header
    next(csvread,None)
    # read the file row by row
    for row in csvread:
        month_count += 1
        if month_count == 1:
            prev_val = int(row[1])
            first_profit = int(row[1])
        net_amount = net_amount + int(row[1])
        tmp_diff = int(row[1]) - prev_val
        if  tmp_diff > greatest_increase:
            greatest_increase = tmp_diff
            greatest_month = str(row[0])

        if (tmp_diff) <= (greatest_decrease):
            greatest_decrease = tmp_diff
            decrease_month = str(row[0])
        prev_val = int(row[1])
        last_profit = int(row[1])
    average_change = (last_profit-first_profit)/(month_count-1)

#print("")
#print("Financial Analysis")
#print("-----------------------------")
print(f"\n Financial Analysis \n ----------------------------- \n Total Months : {month_count} \n Total : ${net_amount} \n Average  Change: ${str(round(average_change,2))} \n Greatest Increase in Profits: {greatest_month} $({greatest_increase}) \n Greatest Decrease in Profits: {decrease_month} $({greatest_decrease})\n\n")

with open("Output.txt", "w") as text_file:
    print(f"\n Financial Analysis \n ----------------------------- \n Total Months : {month_count} \n Total : ${net_amount} \n Average  Change: ${str(round(average_change,2))} \n Greatest Increase in Profits: {greatest_month} $({greatest_increase}) \n Greatest Decrease in Profits: {decrease_month} $({greatest_decrease})\n\n", file=text_file)


