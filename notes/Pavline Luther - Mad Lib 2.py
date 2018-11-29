# ("Dear superintendent, most students would disagree that removing sports from schools is beneficial for students.")
# ("It is clear that sports are good for kids overall.")
# ("Sports keep kids physically fit, engaged at school,")
# ("and teach kids skills that will help them be successful in life.")

# List
words = []

# Inputs
words.append(input("Type in an person : "))  # 0
words.append(input("Type in a plural noun : "))  # 1
words.append(input("Type in a verb that is capitalized and ends in ing  : "))  # 2
words.append(input("Type in the verb not capitalized : "))  # 3
words.append(input("Type in a place : "))  # 4
words.append(input("Type in a noun : "))  # 5
words.append(input("Type in a issue : "))  # 6
words.append(input("Type in a adjective : "))  # 7
words.append(input("Type in a adjective : "))  # 8
words.append(input("Type in a skill : "))  # 9
words.append(input("Type in a skill : "))  # 10
words.append(input("Type in a skill : "))  # 11
words.append(input("Type in a adjective or profession : "))  # 12


# Story
print("Dear %s, most %s would agree that %s from %s is beneficial for %s." % (words[0], words[1], words[3], words[4],
                                                                              words[1]))
print("%s can help %s into becoming a %s. %s prevents issues like %s." % (words[2], words[1], words[5], words[2],
                                                                          words[6]))
print("It is clear that %s is good for %s overall." % (words[3], words[1]))
print("%s keeps %s %s, and %s at %s," % (words[2], words[1], words[7], words[8], words[4]))
print("and teach %s skills like: %s, %s, and %s. This will help them be %s." % (words[1], words[9], words[10],
                                                                                words[11], words[12]))
