# File: statisticsOnNumbers_1.py
# Author: Kirill Nikolaev
# Description: class NumberStats has add_number() and count_numbers() methods

class NumberStats:
    def __init__(self):
        self.__numbers = []  # private attribute

    def add_number(self, number):
        self.__numbers.append(number)

    def count_numbers(self):
        return len(self.__numbers)
    
def main():
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added: ", stats.count_numbers())

main()