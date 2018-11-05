import random
a = random.randint(1, 10)
guess = 5



def grade_calc(answer):
 if number == answer:
  return "Winner Winner Chinken dinner"
 elif number > answer:
  return "You aiming to high"
 elif number < answer:
  return "Not tall enough for this ride"

 your_grade = grade_calc(number)
 print(your_grade)
