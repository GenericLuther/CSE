import random
import string

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

while guesses > 0:
    print(letters)
    print(hidden_answer)
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    if letter in answer_list:
        if word_length is 4:
            if letter is answer_list[0]:
                answer_letters.pop(0)
                answer_letters.insert(0, letter)
                if letter is answer_list[1]:
                    answer_letters.pop(1)
                    answer_letters.insert(1, letter)
                    if letter is answer_list[2]:
                        answer_letters.pop(2)
                        answer_letters.insert(2, letter)
                        if letter is answer_list[3]:
                            answer_letters.pop(3)
                            answer_letters.insert(3, letter)
            if letter is answer_list[1]:
                answer_letters.pop(1)
                answer_letters.insert(1, letter)
                if letter is answer_list[2]:
                    answer_letters.pop(2)
                    answer_letters.insert(2, letter)
                    if letter is answer_list[3]:
                        answer_letters.pop(3)
                        answer_letters.insert(3, letter)
            if letter is answer_list[2]:
                answer_letters.pop(2)
                answer_letters.insert(2, letter)
                if letter is answer_list[3]:
                    answer_letters.pop(3)
                    answer_letters.insert(3, letter)
            if letter is answer_list[3]:
                answer_letters.pop(3)
                answer_letters.insert(3, letter)
        if word_length is 3:
            if letter is answer_list[0]:
                answer_letters.pop(0)
                answer_letters.insert(0, letter)
                if letter is answer_list[1]:
                    answer_letters.pop(1)
                    answer_letters.insert(1, letter)
                    if letter is answer_list[2]:
                        answer_letters.pop(2)
                        answer_letters.insert(2, letter)
            if letter is answer_list[1]:
                answer_letters.pop(1)
                answer_letters.insert(1, letter)
                if letter is answer_list[2]:
                    answer_letters.pop(2)
                    answer_letters.insert(2, letter)
                    if letter is answer_list[2]:
                        answer_letters.pop(2)
                        answer_letters.insert(2, letter)
                        if letter is answer_list[3]:
                            answer_letters.pop(3)
                            answer_letters.insert(3, letter)
        if word_length is 5:
                if letter is answer_list[0]:
                    answer_letters.pop(0)
                    answer_letters.insert(0, letter)
                    if letter is answer_list[1]:
                        answer_letters.pop(1)
                        answer_letters.insert(1, letter)
                        if letter is answer_list[2]:
                            answer_letters.pop(2)
                            answer_letters.insert(2, letter)
                            if letter is answer_list[3]:
                                answer_letters.pop(3)
                                answer_letters.insert(3, letter)
                                if letter is answer_list[4]:
                                    answer_letters.pop(4)
                                    answer_letters.insert(4, letter)
                if letter is answer_list[1]:
                    answer_letters.pop(1)
                    answer_letters.insert(1, letter)
                    if letter is answer_list[2]:
                        answer_letters.pop(2)
                        answer_letters.insert(2, letter)
                        if letter is answer_list[3]:
                            answer_letters.pop(3)
                            answer_letters.insert(3, letter)
                            if letter is answer_list[4]:
                                answer_letters.pop(4)
                                answer_letters.insert(4, letter)
                if letter is answer_list[2]:
                    answer_letters.pop(2)
                    answer_letters.insert(2, letter)
                    if letter is answer_list[3]:
                        answer_letters.pop(3)
                        answer_letters.insert(3, letter)
                        if letter is answer_list[4]:
                            answer_letters.pop(4)
                            answer_letters.insert(4, letter)
                if letter is answer_list[3]:
                    answer_letters.pop(3)
                    answer_letters.insert(3, letter)
                    if letter is answer_list[4]:
                        answer_letters.pop(4)
                        answer_letters.insert(4, letter)
                if letter is answer_list[4]:
                    answer_letters.pop(4)
                    answer_letters.insert(4, letter)
    elif letter not in answer:
        print("Nope")
        guesses -= 1
    letters.append(letter)
    print(answer_letters)









