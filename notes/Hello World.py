
"""
print("Hello World!")
# This is a comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. MAke notes to myself
# 2. COmment pieces of code that do not work
# 3. Make my code easier to read


print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here.")

# Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out..")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one")
print(6 % 2)
print(5 % 2)
print(11 % 4)

# Powers
# What us 2^100
print(2 ** 100)

# Taking input
#name = input ("What is your name?")
#print("Hello %s." % name)

#age = input(" How old are you? >_")
#print ("%s?!? You belong in a museum" % age)
#print()
#print("%s is really old. They are %s years old." % (name, age))

# Variable Assignments
car_name = "Biggerest Boy"
car_type = "F-150"
car_cylinders = 8
car_miles_per_gallon = 0.01


print("I have a car called the %s. It is a %s." % (car_name, car_type))

# Recasting
real_age = int (input("How old are you again?"))
hidden_age = real_age + 5
print("this is your real age: %d" % hidden_age)
"""

"""
This is a multi-line comment
anything between the "s is not run.
"""


#Functions
def sayIt():
    print("Hello World!")


sayIt()
sayIt()
sayIt()

"""
# f(x) = 2x + 3
def f(x):
    print(2^x + 3)

    f(1)
    f(5)
    f(5000)
"""
# Distance Formula


def distance(x1, y1, x2, y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
    print(dist)


distance(0, 0, 3, 4)
distance(0, 0, 5, 12)

"""
# Loops
for i in range(5000):
    #sayIt()

    for i in range(0):
        print(i + 1)


for i in range (5):
"""
"""
# While loops
a = 0
while a < 10:
    print(a)
    a += 2   # This is the same as saying a = a + 1


At the moment you START the loop:
For loops - Use when you know EXACTLY how many iterations 
While loops - Use when you DON'T know how many iterations



def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


your_grade = grade_calc(87)
print(your_grade)

# "Random" Notes

import random
print(random.randint(0, 100))


# Equality Statements
print(5 > 3)
print(5 >= 3)

print(3 == 3)
print(3 != 4)

a = 3  # A is set to 3
a == 3  # Is equal to 3?
"""
# Creating a list
color = ["blue", "turquoise", "pink", "orange","black", "red", "yellow", "purple", "green"] # USE SQUARE BRACKETS!!!!!
print(color)
print(color[1])
print(color[0])

# Length of the list
print("There are %d things in the list." % len(color))

# Changing Elements in a list
color[1] = "cyan"
print(color)

# Looping through lists
for item1 in color:
    print(item1)

shoppinglist = ["TV", "Nintendo", "Phone", "Dinner", "Couch", "DVD Player", "The Second Season Of Spongbob On DVD"]
shoppinglist[2] = "Bed"
for item2 in shoppinglist:
    print(item2)
print(shoppinglist)
print("The last thing in the list is %s" % shoppinglist[len(shoppinglist) - 1])

# Slicing a list
print(shoppinglist[1:3])

food_list = ["pizza", "tacos", "oreo", "lollipops", "noodles", "chicken", "beef", "pork", "calzone", "chicken alfredo",
             "spaghetti", "ravioli", "bacon", "garlic bread", "salad", "cinnamon roll"]

food_list.append("grilled cheese")
food_list.insert(1, "Eggo waffles")
food_list.remove("salad")
print(food_list)

# Tuples
big_list = ["Doctors", "Person", "Surgical Equipment"]
big_list.insert(1, "Grape")
big_list.remove("Person")
print(big_list)

# Also removing stuff from a list
print(food_list)
food_list.pop(8)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list)

for i in range (len(list1)):  # i goes through all indices
    if list1[i] == "u":  # if we find a U
        list1.pop(1)  # remove the i-th index
        list1.insert(1, "a")  # Put a * there instead

# Turn a list into a string
print("".join(list1))
