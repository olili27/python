import random

words_choice = [
    "apple",
    "balloon",
    "cat",
    "dog",
    "elephant",
    "flower",
    "giraffe",
    "house",
    "igloo",
    "jelly",
    "kite",
    "lion",
    "mountain",
    "notebook",
    "orange",
    "penguin",
    "queen",
    "rainbow",
    "sunflower",
    "turtle"
]

name = input("Please your name: ")

print(f"\nGood Luck {name}!\n")

random.shuffle(words_choice)
random.shuffle(words_choice)

word_to_guess = random.choice(words_choice)

chances_to_guess = len(word_to_guess) + int(len(word_to_guess)/2)
print(f"There is a random word of {len(word_to_guess)} characters, guess the characters in it. You have {chances_to_guess} chances.")
guesses = ""

while chances_to_guess > 0:
    character = input("\nGuess a character: ")

    guesses += character
    guessesCopy = guesses
    successes = 0

    for c in word_to_guess:
        if c in guessesCopy:
            index = guessesCopy.index(c)
            guessesCopy = guessesCopy[:index] + guessesCopy[index + 1:]
            successes += 1

            print(c)
        else:
            print("_")
        
    chances_to_guess -= 1

    if successes == len(word_to_guess):
        print("\nCongratulations, You won!\n")
        break

    if chances_to_guess == 0:
        print("You lost!\n")

print(f"The word is {word_to_guess}\n")
