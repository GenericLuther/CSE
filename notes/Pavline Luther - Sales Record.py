import csv
total_profit = float(0)
average_profit = float(0)
average_profit_item = ""
total_profit_item = ""
items = []
with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)
    firstline = True
    for row in reader:
        if firstline is True:
            firstline = False
            continue
        if row[2] in items:
            continue
        else:
            items.append(row[2])
            print(row[2])

