#("Dear superintendent, most students would disagree that removing sports from schools is beneficial for students.")
#("It is clear that sports are good for kids overall.")
#("Sports keep kids physically fit, engaged at school,")
# ("and teach kids skills that will help them be successful in life.")

recipient = "Obama"
people = "turtles"
# verb1 has to end in "ing" and the first letter has to be capitalized
# verb2 is the same as verb 1 just not capitalized
verb1 = "Eating mangos"
verb2 = "eating mangos"
place = "Aunt Bertha's house"
noun = "chunky monkey"
issue = "living for a long of time"
adjective1 = "obese"
adjective2 = "dead"
skill1 = "cosmology "
skill2 = "freestyle dancing"
skill3 = "martial arts"
adjective_or_plural_noun = "astronauts"

# Story
print("Dear %s, most %s would agree that %s from %s is beneficial for %s." % (recipient, people, verb2, place, people))
print("%s can help %s into becoming a %s. %s prevents issues like %s." % (verb1, people, noun, verb1, issue))

print("It is clear that %s is good for %s overall." % (verb2, people))
print("%s keep %s %s, and %s at %s," % (verb1, people, adjective1, adjective2, place))
print("and teach %s skills like: %s, %s, and %s. This will help them be %s." % (people, skill1, skill2, skill3, adjective_or_plural_noun))
