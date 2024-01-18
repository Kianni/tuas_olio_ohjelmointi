# File name: rockScissorsPaper.py
# Author: Kirill
# Description: Rock-Paper-Scissors game. 
# is being played until either user or the computer gets 3 wins.

import random

CHOICES = {"R": "rock", "P": "paper", "S": "scissors"}

RESULT = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
MESSAGES = {"rock": "Rock breaks Scissors", "paper": "Paper covers Rock", "scissors": "Scissors cuts Paper"}

def get_winner(user_choice, computer_choice):
    user_choice = CHOICES[user_choice.upper()]
    if user_choice == computer_choice:
        print("It's a tie!")
        return "Draw"
    elif RESULT[user_choice] == computer_choice:
        print(MESSAGES[user_choice])
        return "User"
    else:
        print(MESSAGES[computer_choice])
        return "Computer"

def print_final_results(user_score, computer_score):
    if user_score == 3:
        print("You won the game")
    else:
        print("You lost!")

def make_a_choice():
    user_choice = input("Give your choice (R, P, S): ")
    computer_choice = random.choice(list(CHOICES.values()))
    print("Computer's choice is:", computer_choice)
    return user_choice, computer_choice

def main():
    user_score = 0
    computer_score = 0
    while user_score < 3 and computer_score < 3:
        user_choice, computer_choice = make_a_choice()
        winner = get_winner(user_choice, computer_choice)
        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1
        print("Computer ", computer_score, ", You ", user_score)
    print_final_results(user_score, computer_score)

main()