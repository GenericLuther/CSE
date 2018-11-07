#("Dear superintendent, most students would disagree that removing sports from schools is beneficial for students.")
#("It is clear that sports are good for kids overall.")
#("Sports keep kids physically fit, engaged at school,")
# ("and teach kids skills that will help them be successful in life.")

recipient = input("Type in an person : ")
people = input("Type in an a plural noun : ")
# verb1 has to end in "ing" and the first letter has to be capitalized
# verb2 is the same as verb 1 just not capitalized
verb1 = input("Type in an a verb that is capitalized  : ")
verb2 = input("Type in the verb not capitalized : ")
place = input("Type in an a place : ")
noun = input("Type in an a noun : ")
issue = input("Type in an a issue : ")
adjective1 = input("Type in an a adjective : ")
adjective2 = input("Type in an a adjective : ")
skill1 = input("Type in an a skill : ")
skill2 = input("Type in an a skill : ")
skill3 = input("Type in an a skill : ")
# feeling or a group
adjective_or_plural_noun = input("Type in an a adjective or profession : ")

# Story
print("Dear %s, most %s would agree that %s from %s is beneficial for %s." % (recipient, people, verb2, place, people))
print("%s can help %s into becoming a %s. %s prevents issues like %s." % (verb1, people, noun, verb1, issue))
print("It is clear that %s is good for %s overall." % (verb2, people))
print("%s keeps %s %s, and %s at %s," % (verb1, people, adjective1, adjective2, place))
print("and teach %s skills like: %s, %s, and %s. This will help them be %s." % (people, skill1, skill2, skill3, adjective_or_plural_noun))
