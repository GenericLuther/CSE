import random
a = random.randint(1, 10)
number = (int(input("Guess the number: ")))

playing = True
guesses = 5
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
    else:
        print("Winner Winner Chicken Dinner")
        playing = False