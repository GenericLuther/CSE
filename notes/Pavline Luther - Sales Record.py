import csv

with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)
    firstline = True
    for row in reader:
        if firstline:
            firstline = False
            continue
        profit = row[13]
        most_profit = float(0)
        if float(most_profit) < float(profit):
            most_profit = profit
        else:
            continue
    print("The largest profit is: %s" % most_profit)
