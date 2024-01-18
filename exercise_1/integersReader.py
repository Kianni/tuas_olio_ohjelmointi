# File name: integersReader.py
# Author: Kirill
# Description: repeatedly reads integers until the user enters 0. Print out the number of negative integers


def main():
    negative = 0
    even = 0
    sum_divisible_by_three = 0
    number = int(input("Enter a number: "))
    while number != 0:
        if number < 0:
            negative += 1
        if number % 2 == 0:
            even += 1
        if number > 0 and number % 3 == 0:
            sum_divisible_by_three += number
        number = int(input("Enter a number: "))
    print("Number of negative integers:", negative)
    print("Number of even integers:", even)
    print("Sum of positive integers divisible by three:", sum_divisible_by_three)

main()