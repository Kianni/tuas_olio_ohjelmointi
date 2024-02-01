# File: statisticsOnNumbers.py
# Author: Kirill Nikolaev
# Description: class NumberStats has add_number() and count_numbers() methods

class NumberStats:
    def __init__(self):
        self.__numbers = []  # private attribute

    def add_number(self, number):
        self.__numbers.append(number)

    def count_numbers(self):
        return len(self.__numbers)
    
    def get_sum(self):
        if self.count_numbers() == 0:
            return 0
        return sum(self.__numbers)
    
    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()
    
def main():
    stats = NumberStats()
    number = int(input("Enter an integer number (-1 to stop): "))
    while number != -1:
        stats.add_number(number)
        number = int(input("Enter an integer number (-1 to stop): "))
    print("Sum of numbers: ", stats.get_sum())
    print("Mean of numbers: ", stats.average())

if __name__ == "__main__":
    main()