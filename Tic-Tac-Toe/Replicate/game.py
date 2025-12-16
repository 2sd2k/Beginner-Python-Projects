from re import X
from player import HumanPlayer, ComputerPlayer
import math
import time

def play_game():
    # Make board
    
    # Ask player to go first
    
    
    # Ask computer to go

# x | x | x 
# 1 | 2 | 3
# ----------
# 4 | 5 | 6 
# ----------
# 7 | 8 | 9
def make_board(player_move=None, comp_move=None):
    # Make a list
    board = []
    count = 1
    for i in range(5):
        if i%2 == 1:
            row = ["-" * 10]
            board.append(row)
            continue
        else:
            row = [f"{count} | {count+1} | {count+2}"]
            count += 3
                
        
        
                
    
#def make_move():  
#def print_board():
    
def main():
    