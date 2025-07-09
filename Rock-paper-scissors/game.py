#Rock-paper-scissors

import random

def play():

    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    # user picked r
    if(user == 'r'):
        if(computer == 'r'):
            print("It was a tie!")
        elif(computer == 'p'):
            print("You lost!")
        else:
            print("You won!")

    elif(user == 'p'):
        if(computer == 'p'):
            print("It was a tie!")
        elif(computer == 's'):
            print("You lost!")
        else:
            print("You won!")

    elif(user == 's'):
        if(computer == 's'):
            print("It was a tie!")
        elif(computer == 'r'):
            print("You lost!")
        else:
            print("You won!")

play()