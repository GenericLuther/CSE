import random

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]
answer = random.choice(words)
guesses = 8
letters = []
if len(answer) is 3:
    print()
print("This Hangman You Know The Rules")
while guesses > 0:
    print(letters)
    print("You Have %d Wrong Guesses Left: " % guesses)
    letter = input()
    print(answer)
    if letter in answer:
        print()
        letters.append(letter)
    elif letter not in answer:
        print("Nope")
        guesses -= 1
        letters.append(letter)










