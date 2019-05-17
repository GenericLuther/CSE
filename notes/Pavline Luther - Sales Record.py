import csv
total_profit = float(0)
average_profit = float(0)
average_profit_item = ""
total_profit_item = ""
items = ['Fruits', 'Clothes', 'Meat', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks', 'Personal Care',
         'Household', 'Vegetables', 'Baby Food', 'Cereal']
firstline = True

with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)

    for row in reader:
        if row[2] == 'Fruits':
            if float(row[13]) > float(total_profit):
                total_profit = row[13]
    print(total_profit)