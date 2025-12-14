import random
from words import words


def hangman():
    word = (random.choice(words)).upper()
    guessed_letters = []
    word_completion = "_" * len(word)
    lives = 6

    while (lives != 0) and word_completion != word:
        print(f"You have {lives} lives left and have used these letters: {' '.join(guessed_letters)}")
        print(f"Current word: {word_completion}\n")
        guess = (input("Guess a letter: ")).upper()
        print()

        if guess in word:
            word_completion_list = list(word_completion)
            for i, letter in enumerate(word):
                if(letter == guess):
                    word_completion_list[i] = guess
            word_completion = "".join(word_completion_list)
        else: 
            print(f"Your letter, {guess} is not in the word.")
            lives -= 1
        
        guessed_letters.append(guess)
        if(lives == 0):
            print(f"Sorry, you died. The word was {word}")
        if word_completion == word:
            print(f"Yay, you guessed the word, {word} !!")

hangman()
