import random

words = ["dog", "cat", "house", "home", "ball", "bay", "bat", "glass", "cable", "hand", "can", "mad"]  # Word Bank
answer = random.choice(words)  # Randomly Selects Word From Word Bank
answer_list = list(answer)
answer_list2 = []
word_length = len(answer)  # Length of the Word
guesses = 8  # Number of Incorrect Guesses Left
letters = []  # Letters That Have Been Guessed
print("This Hangman You Know The Rules")
while guesses > 0:
    print(letters)
    letter = input("You Have %d Wrong Guesses Left: " % guesses)
    if letter in answer:
        if letter is answer_list[0]:
            answer_list2.insert(0, letter)
            if letter is answer_list[1]:
                answer_list2.insert(1, letter)
                if letter is answer_list[2]:
                    answer_list2.insert(2, letter)
                    if letter is answer_list[3]:
                        answer_list2.insert(3, letter)
                        if letter is answer_list[4]:
                            answer_list2.insert(4, letter)
                            if letter is answer_list[5]:
                                answer_list2.insert(5, letter)
        letters.append(letter)
    elif letter not in answer:
        print("Nope")
        guesses -= 1

        letters.append(letter)










