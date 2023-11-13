import random
import sys

# Set some variables
wordList = ["lioness", "umbrella", "window", "computer", "glass",
            "juice", "chair", "desktop", "laptop", "dog", "cat", "lemon", "cable",
            "mirror", "hat"]
guess_word = []
secretWord = random.choice(wordList)  # Randomize single word from the list
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []


def beginning():
    print("Hello Mate!\n")
    while True:
        name = input("Please enter Your name\n").strip()
        if name == '':
            print("You can't do that! No blank lines")
        else:
            break


beginning()


def newFunc():
    print("Well, that's the perfect moment to play some Hangman!\n")
    while True:
        gameChoice = input("Would You?\n").upper()
        if gameChoice == "YES" or gameChoice == "Y":
            break
        elif gameChoice == "NO" or gameChoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue


newFunc()


def change():
    for character in secretWord:  # Printing blanks for each letter in secret word
        guess_word.append("-")
    print("Ok, so the word You need to guess has", length_word, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print(guess_word)


change()


def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter\n").lower()
        # Checking input
        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        # Checking if letter has been already used
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                print(guess_word)
                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
    if guess_taken == 10:
        print("Sorry Mate, You lost :<! The secret word was", secretWord)


guessing()
print("Game Over!")
