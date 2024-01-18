# File name: returnRandomNumber.py
# Author: Kirill
# Description: function returns random number after being called

import random

def return_random_number():
    return random.randint(1, 100)

def main():
    print(return_random_number())
    print(return_random_number())
    print(return_random_number())
    print(return_random_number())
    print(return_random_number())
    print(return_random_number())
    print(return_random_number())

main()