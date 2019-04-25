# import csv
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print ("Writing File...  ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]
#             new_number = old_number + 1
#             row[0] = new_number
#             writer.writerow(row)
#             # print(int(old_number) + 1)
#             # print (old_number)
# print("OK")

import csv

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print ("Writing File...  ")
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        for row in reader:
            old_number = row[0]   # This is a string
            first_num = int(old_number[0])  # This is the first
            if first_num % 2 == 0:
                writer.writerow(row)
            # print(int(old_number) + 1)
            # print (old_number)
print("OK")
