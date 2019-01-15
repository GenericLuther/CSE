import random

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]
answer = random.choice(words)
guesses = 8
print("This Hangman You Know The Rules")
if answer is "dog":
    answer2 = "dog"    

while guesses > 0:
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    print(answer)
    if letter in answer:
        print(letter)
