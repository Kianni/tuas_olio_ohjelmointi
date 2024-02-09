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

    mammal1 = Mammal(1, "Elephant", "Dumbo", 3.5, 5000)
    mammals = [
        Mammal(1, "Mouse", "Small", 1, 0.1),
        Mammal(2, "Cat", "Medium", 3, 4.5),
        Mammal(3, "Dog", "Large", 8, 30),
        Mammal(4, "Wolf", "Large", 15, 80),
        Mammal(5, "Bear", "Large", 100, 500),
        Mammal(6, "Elephant", "Huge", 1200, 6000),
        Mammal(7, "Blue Whale", "Gigantic", 10000, 200000),
    ]

    player1 = Player(player1_name, 1, None)
    player2 = Player(player2_name, 2, None)

    for player in [player1, player2]:
        dice1, dice2 = Dice(), Dice()
        dice1.roll()
        dice2.roll()
        sum = dice1.get_side() + dice2.get_side()
        player.mammal = mammals[min(sum, len(mammals)) - 1]
        print(f"{player.name} rolled {sum} and got a {player.mammal.species}")

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