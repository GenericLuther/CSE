import random
a = random.randint(1, 25)
number = (int(input("Guess a number between 1 and 25: ")))

playing = True
guesses = 4
while guesses > 0 and playing:
    if number > a:
        print("You over shot")
        guesses -= 1
        number = (int(input("Guess another number: ")))
        print()
    if number < a:
        print("Not tall enough for this ride")
        guesses -= 1
        number = (int(input("Guess another number: ")))
        print()
    if number == a:
        print("Victory Royale #1")
        print("Winner Winner Chicken Dinner")
        playing = False
    elif guesses == 0:
        print("OOPS ERROR 404 CORRECT ANSWER NOT FOUND :(")
        print("Just Kidding it was %s" % a)