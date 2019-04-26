import csv
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
#
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         print ("Writing File...  ")
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         for row in reader:
#             old_number = row[0]   # This is a string
#             first_num = int(old_number[0])  # This is the first
#             if first_num % 2 == 0:
#                 writer.writerow(row)
#             # print(int(old_number) + 1)
#             # print (old_number)
# print("OK")
#
#
# with open("Book1.csv", 'r') as old_csv:
#     with open("MyNewFile.csv", 'w', newline='') as new_csv:
#         reader = csv.reader(old_csv)
#         writer = csv.writer(new_csv)
#         print("Processing...  ")
#
#         for row in reader:
#             # old_number = int(row[0]) + 1
#             old_number = row[0]   # This is a string
#             first_num = int(old_number[0])  # This is the first
#             if first_num % 3 == 0:
#                 writer.writerow(row)
#     print("Done")


def validate(num: str):
    first_num = int(num[0])
    if not all_16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def all_16_digits(num: str)


# def validate(num: str):
#     first_num = int(num[0])
#     if first_num % 3 == 0 and first_num % 2 == 0:
#         return True
#     return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Work yes")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]
            if validate(old_number) is True:
                writer.writerrow(row)
    print("Done")
