# File name: rockScissorsPaper.py
# Author: Kirill
# Description: Rock-Paper-Scissors game. 
# is being played until either user or the computer gets 3 wins.

import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Draw")
        return "Draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win")
        return "User"
    else:
        print("Computer wins")
        return "Computer"

def print_final_results(user_score, computer_score):
    if user_score == 3:
        print("You won the game")
    else:
        print("Computer won the game")
    print("Final score: Computer -", computer_score, ", You -", user_score)

def make_a_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print("Computer's choice:", computer_choice)
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
        print("Score: Computer -", computer_score, ", You -", user_score)
    print_final_results(user_score, computer_score)

main()