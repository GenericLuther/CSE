import csv
total_profit = float(0)
average_profit = float(0)
average_profit_item = ""
total_profit_item = ""
items = []


def products():
    firstline = True
    for row in reader:
        if firstline is True:
            firstline = False
            continue
        if row[2] in items:
            continue
        else:
            items.append(row[2])
    return items


def profit():
    firstline = True
    for row in reader:
        if firstline is True:
            firstline = False
            continue
        else:
            if float(row[13]) > total_profit:
                total_profit_1 = float(row[13])
                profitable_item = row[2]
                print(profitable_item)
                print(total_profit_1)


with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)

    for row in reader:
        products()
        profit()
