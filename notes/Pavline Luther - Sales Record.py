import csv
import hack
most_profit = float(0)
with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)
    firstline = True
    for row in reader:
        if firstline:
            firstline = False
            continue
        profit = row[13]
        if most_profit < float(profit):
            most_profit = float(profit)
            print(most_profit)
        else:
            continue
    print("The largest profit is: %s" % most_profit)

