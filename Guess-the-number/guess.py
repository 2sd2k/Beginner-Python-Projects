# guess the number
import random

def guess(x):
    number = random.randint(1, x)
    user_number = 0
    while user_number != number: 
        user_number = int(input(f"Guess a number between 1 and {x}: "))
        if(user_number < number):
            print("Sorry, guess again. Too low.")
        elif(user_number > number):    
            print("Sorry, guess again. Too high.")
        else:
            print(f"Yay, congrats. You have guessed the number {number} correctly!! ")

def computer_guess(x):
    low = 1
    high = x
    guess = random.randint(low, high)
    answer = ""
    while(answer.upper() != "C"):
        guess = random.randint(low, high)
        answer = (input(f"Is {guess} too high (H), too low (L), or correct(C)?? ")).upper()
        if(answer == 'H'):
            high = guess
        elif(answer == 'L'):
            low = guess
        elif(answer == 'C'):
            print(f"Yay! The computer guessed your number, {guess}, correctly! ")


computer_guess(10)