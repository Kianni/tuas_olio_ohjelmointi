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
    stats_all = NumberStats()
    stats_even = NumberStats()
    stats_odd = NumberStats()

    number = int(input("Enter an integer number (-1 to stop): "))
    while number != -1:
        stats_all.add_number(number)
        if number % 2 == 0:
            stats_even.add_number(number)
        else:
            stats_odd.add_number(number)
        number = int(input("Enter an integer number (-1 to stop): "))

    print("Sum of numbers: ", stats_all.get_sum())
    print("Mean of numbers: ", stats_all.average())
    print("Sum of even numbers: ", stats_even.get_sum())
    # print("Mean of even numbers: ", stats_even.average())
    print("Sum of odd numbers: ", stats_odd.get_sum())
    # print("Mean of odd numbers: ", stats_odd.average())

if __name__ == "__main__":
    main()