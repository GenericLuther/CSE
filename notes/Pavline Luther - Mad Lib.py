#("Dear superintendent, most students would disagree that removing sports from schools is beneficial for students.")
#("It is clear that sports are good for kids overall.")
#("Sports keep kids physically fit, engaged at school,")
# ("and teach kids skills that will help them be successful in life.")

recipient = input("Type in an person : ")
people = input("Type in an a noun : ")
# verb1 has to end in "ing" and the first letter has to be capitalized
# verb2 is the same as verb 1 just not capitalized
verb1 = input("Type in an a verb that is  : ")
verb2 = input("Type in an : ")
place = input("Type in an : ")
noun = input("Type in an : ")
issue = input("Type in an : ")
adjective1 = input("Type in an : ")
adjective2 = input("Type in an : ")
skill1 = input("Type in an : ")
skill2 = input("Type in an : ")
skill3 = input("Type in an : ")
# feeling or a group
adjective_or_plural_noun = input("Type in an : ")

# Story
print("Dear %s, most %s would agree that %s from %s is beneficial for %s." % (recipient, people, verb2, place, people))
print("%s can help %s into becoming a %s. %s prevents issues like %s." % (verb1, people, noun, verb1, issue))

print("It is clear that %s is good for %s overall." % (verb2, people))
print("%s keep %s %s, and %s at %s," % (verb1, people, adjective1, adjective2, place))
print("and teach %s skills like: %s, %s, and %s. This will help them be %s." % (people, skill1, skill2, skill3, adjective_or_plural_noun))
