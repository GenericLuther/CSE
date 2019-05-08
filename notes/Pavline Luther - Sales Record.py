import csv

with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)
    for row in reader:
        profit = row[13]
        most_profit = float(0)
        if profit == 'Total Profit':
            pass
        if float(profit) > most_profit:
            most_profit = profit
    print("The largest profit is: %d" % most_profit)
