import random

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]
answer = random.choice(words)
guesses = 8

while guesses > 0:
    print("This Hangman You Know The Rules")
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    print(letter)