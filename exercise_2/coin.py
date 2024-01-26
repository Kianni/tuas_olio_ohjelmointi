# File: coin.py
# Source: OOP in Python course by TUAS
# Modified by: Kirill Nikolaev
# Description: Coin object and tossing

import random

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        if random.randint(0, 1) == 0:
            self.sideup = "Heads"
        else:
            self.sideup = "Tails"

    def get_sideup(self):
        return self.sideup
    
def main():
    my_coin = Coin()

    print('This side is up:', my_coin.get_sideup())
    print('Tossing the coin...')

    my_coin.toss_the_coin()

    print('This side is up:', my_coin.get_sideup())

main()