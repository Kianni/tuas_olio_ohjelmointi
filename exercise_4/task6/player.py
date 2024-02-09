# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: Player

from dice import Dice

class Player:
    def __init__(self, name, player_id):
        self.__name = name
        self.__player_id = player_id
        self.__dice = Dice()

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def player_id(self):
        return self.__player_id
    
    @player_id.setter
    def player_id(self, player_id):
        self.__player_id = player_id

    @property
    def dice(self):
        return self.__dice
    
    @dice.setter
    def dice(self, dice):
        self.__dice = dice

    def __str__(self) -> str:
        return f"Player {self.__name} with {self.__player_id}"
    

def two_players_game(players):
    (player1, player2) = players.values()
    while True:

        # Player 1 turn
        print(f"{player1.name}, press Enter to roll the dice...")
        input()
        player1.dice.roll()
        print(f"{player1.name} rolled {player1.dice.get_side()}")

        # Player 2 turn
        print(f"{player2.name}, press Enter to roll the dice...")
        input()
        player2.dice.roll()
        print(f"{player2.name} rolled {player2.dice.get_side()}")

        if player1.dice.get_side() != player2.dice.get_side():
            break
        else:
            print("It's a tie! Roll again!")

    if player1.dice.get_side() > player2.dice.get_side():
        print(f"{player1.name} WON!!!")
    else:
        print(f"{player2.name} WON!!!")

def main():
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")

    player1 = Player(player1_name, 1)
    player2 = Player(player2_name, 2)

    players = {
        1: player1,
        2: player2
    }
    two_players_game(players)

if __name__ == "__main__":
    main()