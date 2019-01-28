import random

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]  # Word Bank
answer = random.choice(words)  # Randomly Selects Word From Word Bank
answer_list = list(answer)
word_length = len(answer)  # Length of the Word
guesses = 8  # Number of Incorrect Guesses Left
letters = []  # Letters That Have Been Guessed
print("This Hangman You Know The Rules")
print("This word has %d letters" % word_length)
hidden_answer = ('_'*word_length)
answer_letters = list(hidden_answer)
playing = True
win = False
while playing is True:
    answer_string = ''.join(answer_letters)
    if answer_string == answer:
        playing = False
        win = True
        continue
    print("Letters you have guessed: %s" % letters)
    if letters == answer:
        playing = False
        win = True
        continue
    print(answer_string)
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    letters.append(letter)
    if letter in answer_list:
        for i in range(len(answer_list)):
            if letter is answer_list[i]:
                answer_letters.pop(i)
                answer_letters.insert(i, letter)
    elif letter not in answer:
        print("Nope")
        guesses -= 1
    if guesses <= 0:
        playing = False
if win:
    print("You Did it, You Spelled the Word")
else:
    print("RIP You Lost")
