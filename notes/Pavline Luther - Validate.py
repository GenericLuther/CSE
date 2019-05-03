import csv


def sixteen_digits(num):
    if len(list(num)) == 16:
        return True
    return False


def remove0(num):
    num_list = list(num)
    num_list.pop(15)
    return num_list


def reverse_it(num):
    reverse_num = num[::-1]
    return reverse_num


def divisible_by_2(num):
    num = int(num[0])
    if num % 2 == 0:
        return True
    return False


def complicated_thing(num):
    num = list(num)
    for idx in range(len(num)):
        if divisible_by_2(str(idx)) is True:
            num[idx] = str(int(num[idx]) * 2)
    return num


def over9(num):
    num = list(num)
    for idx in range(len(num)):
        if int(num[idx]) > 9:
            num[idx] = str(int(num[idx]) - 9)
    return num


def add_all(num):
    num = list(num)
    aggregate = 0
    for idx in range(len(num)):
        aggregate += int(num[idx])
    return aggregate


def mod_10(num):
    modnum = num % 10
    return modnum


def valid_card_number(num):
    if sixteen_digits(num) is True:
        old_num_list = list(num)
        # print("old_num")
        # print(old_num_list)
        drop_num_list = remove0(old_num_list)
        # print("drop num")
        # print(drop_num_list)
        reverse_num_list = reverse_it(drop_num_list)
        # print("reverse_num")
        # print(reverse_num_list)
        complicated_num_list = complicated_thing(reverse_num_list)
        # print("complicated_num")
        # print(complicated_num_list)
        over9_num_list = over9(complicated_num_list)
        # print("over9")
        # print(over9_num_list)
        aggregate = add_all(over9_num_list)
        # print("aggregate")
        # print(aggregate)
        modnum = mod_10(aggregate)
        # print("modnum")
        # print(modnum)
        if str(modnum) == old_num_list[15]:
            return True
        else:
            print('Invalid Number: ' + num)
            return False
    else:
        print('Invalid Number: ' + num)
        return False


with open("Book1.csv", 'r') as old_csv:
    print("Thinking...")
    y = 0
    x = 0
    reader = csv.reader(old_csv)
    for row in reader:
        old_number = row[0]
        valid_card_number(old_number)
        if valid_card_number(old_number) is False:
            x += 1
        elif valid_card_number(old_number) is True:
            y += 1

print("Invalid Credit Card Numbers- %d" % x)
print("Invalid Invalid Credit Card Numbers- %d" % y)
print('Fin')
