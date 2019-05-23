import csv
total_profit_fruit = float(0)
average_profit_fruit = float(0)
total_items_fruit = 0
total_profit_clothes = float(0)
average_profit_clothes = float(0)
total_items_clothes = 0
total_profit_meat = float(0)
average_profit_meat = float(0)
total_items_meat = 0
total_profit_beverages = float(0)
average_profit_beverages = float(0)
total_items_beverages = 0
total_profit_office = float(0)
average_profit_office = float(0)
total_items_office = 0
total_profit_cosmetics = float(0)
average_profit_cosmetics = float(0)
total_items_cosmetics = 0
total_profit_snacks = float(0)
average_profit_snacks = float(0)
total_items_snacks = 0
total_profit_care = float(0)
average_profit_care = float(0)
total_items_care = 0
total_profit_house = float(0)
average_profit_house = float(0)
total_items_house = 0
total_profit_veg = float(0)
average_profit_veg = float(0)
total_items_veg = 0
total_profit_babyfd = float(0)
average_profit_babyfd = float(0)
total_items_babyfd = 0
total_profit_cereal = float(0)
average_profit_cereal = float(0)
total_items_cereal = 0
items = ['Fruits', 'Clothes', 'Meat', 'Beverages', 'Office Supplies', 'Cosmetics', 'Snacks', 'Personal Care',
         'Household', 'Vegetables', 'Baby Food', 'Cereal']
firstline = True

with open("Sales Records.csv", 'r') as profit_csv:
    print("Thinking...")
    reader = csv.reader(profit_csv)
    for row in reader:
        if firstline is True:
            firstline = False
            continue
        if row[2] == 'Fruits':
                total_profit_fruit += float(row[13])
                total_items_fruit += 1
        if row[2] == 'Clothes':
                total_profit_clothes += float(row[13])
                total_items_clothes += 1
        if row[2] == 'Meat':
                total_profit_meat += float(row[13])
                total_items_meat += 1
        if row[2] == 'Beverages':
                total_profit_beverages += float(row[13])
                total_items_beverages += 1
        if row[2] == 'Office Supplies':
                total_profit_office += float(row[13])
                total_items_office += 1
        if row[2] == 'Cosmetics':
                total_profit_cosmetics += float(row[13])
                total_items_cosmetics += 1
        if row[2] == 'Snacks':
                total_profit_snacks += float(row[13])
                total_items_snacks += 1
        if row[2] == 'Personal Care':
                total_profit_care += float(row[13])
                total_items_care += 1
        if row[2] == 'Household':
                total_profit_house += float(row[13])
                total_items_house += 1
        if row[2] == 'Vegetables':
                total_profit_veg += float(row[13])
                total_items_veg += 1
        if row[2] == 'Baby Food':
                total_profit_babyfd += float(row[13])
                total_items_babyfd += 1
        if row[2] == 'Cereal':
                total_profit_cereal += float(row[13])
                total_items_cereal += 1
        else:
            continue
average_profit_fruit = total_profit_fruit / total_items_fruit
average_profit_clothes = total_profit_clothes / total_items_clothes
average_profit_meat = total_profit_meat / total_items_meat
average_profit_beverages = total_profit_beverages / total_items_beverages
average_profit_office = total_profit_office / total_items_office
average_profit_cosmetics = total_profit_cosmetics / total_items_cosmetics
average_profit_snacks = total_profit_snacks / total_items_snacks
average_profit_care = total_profit_care / total_items_care
average_profit_house = total_profit_house / total_items_house
average_profit_veg = total_profit_veg / total_items_veg
average_profit_babyfd = total_profit_babyfd / total_items_babyfd
average_profit_cereal = total_profit_cereal / total_items_cereal
print("Fruit")
print("Total: %s" % total_profit_fruit)
print("Average: %s" % average_profit_fruit)
print("Clothes")
print("Total: %s" % total_profit_clothes)
print("Average: %s" % average_profit_clothes)
print("Meat")
print("Total: %s" % total_profit_meat)
print("Average: %s" % average_profit_meat)
print("Beverages")
print("Total: %s" % total_profit_beverages)
print("Average: %s" % average_profit_beverages)
print("Office Supplies")
print("Total: %s" % total_profit_office)
print("Average: %s" % average_profit_office)
print("Cosmetics")
print("Total: %s" % total_profit_cosmetics)
print("Average: %s" % average_profit_cosmetics)
print("Snacks")
print("Total: %s" % total_profit_snacks)
print("Average: %s" % average_profit_snacks)
print("Personal Care")
print("Total: %s" % total_profit_care)
print("Average: %s" % average_profit_care)
print("Household")
print("Total: %s" % total_profit_house)
print("Average: %s" % average_profit_house)
print("Vegetables")
print("Total: %s" % total_profit_veg)
print("Average: %s" % average_profit_veg)
print("Baby Food")
print("Total: %s" % total_profit_babyfd)
print("Average: %s" % average_profit_babyfd)
print("Cereal")
print("Total: %s" % total_profit_cereal)
print("Average: %s" % average_profit_cereal)


# ComputerNum: 33
