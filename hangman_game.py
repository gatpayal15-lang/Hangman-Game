#HANGMAN GAME 
import random

# Step 1: Word list
words = ["apple", "banana", "grapes", "mango", "peach"]

# Step 2: Random word
word = random.choice(words)

# Step 3: Blank display
guessed = ["_"] * len(word)

# Step 4: Attempts
attempts = 6

print("🎮 Welcome to Hangman Game!")

while attempts > 0:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    letter = input("Enter a letter: ").lower()

    # Check if letter in word
    if letter in word:
        print(" Correct guess!")

        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        print("Wrong guess!")
        attempts -= 1

    # Check win
    if "_" not in guessed:
        print("\n You WON! Word was:", word)
        break

# If attempts finished
if attempts == 0:
    print("\n You LOST! Word was:", word)