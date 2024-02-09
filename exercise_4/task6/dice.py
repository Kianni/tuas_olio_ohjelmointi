# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: Dice

import random

class Dice:
    def __init__(self):
        self.side = 1

    def roll(self):
        self.side = random.randint(1, 6)

    def get_side(self):
        return self.side
    
def roll_dices(dices):
    sum = 0
    sides = []
    for dice in dices:
        dice.roll()
        sides.append(dice.get_side())
        sum += dice.get_side()
    return sum, sides

def player_turn(dices, player_name):
    sum = 0
    print(f"{player_name}, press Enter to roll the dices...")
    input()
    sum, sides = roll_dices(dices)
    print(f"{player_name} rolled {sum} with sides {sides}")
    if sum == 6 * len(dices):
        print(f"Congratulations, {player_name}! You rolled the best possible sum {sum}!")        
    return sum

def play_game(dices):
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")

    while True:
        player1_sum = player_turn(dices, player1_name)
        player2_sum = player_turn(dices, player2_name)
        if player1_sum != player2_sum:
            break
        else:
            print("It's a tie! Roll again!")

    if player1_sum > player2_sum:
        print(f"{player1_name} WON!!!")
    else:
        print(f"{player2_name} WON!!!")

def main():
    amount_of_dices = input("Enter the amount of dices: ")
    dices = [Dice() for _ in range(int(amount_of_dices))]
    play_game(dices)

if __name__ == "__main__":
    main()
