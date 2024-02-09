# File: player.py
# Author: Kirill Nikolaev
# Description: Player

from dice import Dice
from mammal import Mammal

class Player:
    def __init__(self, name, player_id, mammal):
        self.__name = name
        self.__player_id = player_id
        self.__dice = Dice()
        self.__mammal = mammal

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

    @property
    def mammal(self):
        return self.__mammal
    
    @mammal.setter
    def mammal(self, mammal):
        self.__mammal = mammal

    def __str__(self) -> str:
        return f"Player {self.__name} with ID {self.__player_id}"
    

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
        print(f"{player1} WON!!!")
    else:
        print(f"{player2} WON!!!")

def main():
    player1_name = input("Enter the name of the first player: ")
    player2_name = input("Enter the name of the second player: ")

    wolf = Mammal(1, "Canis lupus", "Wolf", "Large", 80)
    bear = Mammal(2, "Ursus arctos", "Bear", "Large", 500)

    player1 = Player(player1_name, 1, wolf)
    player2 = Player(player2_name, 2, bear)

    print("Players and their mammals:")

    print("{:<20} {:<20} {:<20} {:<20} {:<20}".format('Player ID', 'Name', 'Species', 'Size', 'Weight'))
    print('-' * 100)
    for player in [player1, player2]:
        mammal = player.mammal
        print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(player.player_id, player.name, mammal.species, mammal.size, mammal.weight))

    players = {
        1: player1,
        2: player2
    }
    two_players_game(players)

if __name__ == "__main__":
    main()