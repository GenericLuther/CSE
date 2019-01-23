import random
import string

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]  # Word Bank
answer = random.choice(words)  # Randomly Selects Word From Word Bank
answer_list = list(answer)
answer_letters = []
word_length = len(answer)  # Length of the Word
guesses = 8  # Number of Incorrect Guesses Left
letters = []  # Letters That Have Been Guessed
print("This Hangman You Know The Rules")
print("This word has %d letters"% word_length)
while guesses > 0:
    print(letters)
    print('_'*word_length)
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    if letter in answer_list:
        if letter in
    elif letter not in answer:
        print("Nope")
        guesses -= 1

        letters.append(letter)
    print(answer_letters)









