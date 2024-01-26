# File: coin.py
# Source: OOP in Python course by TUAS
# Modified by: Kirill Nikolaev
# Description: Coin object and tossing

import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        outcome = random.randint(0, 4)
        if outcome == 0:
            self.sideup = "Heads"
        elif outcome == 1:
            self.sideup = "Tails"
        elif outcome == 2:
            self.sideup = "Upright on table"
        elif outcome == 3:
            self.sideup = "Disappeared in rabbit hole"
        else:
            self.sideup = "Lost in wormhole in space"

    def get_sideup(self):
        return self.sideup
    
def main():
    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())
    print('Tossing the coin...')

    my_coin.toss_the_coin()

    print('This side is up:', my_coin.get_sideup())

main()