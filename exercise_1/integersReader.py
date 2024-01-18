# File name: integersReader.py
# Author: Kirill
# Description: repeatedly reads integers until the user enters 0. Print out the number of negative integers


def main():
    negative = 0
    number = int(input("Enter a number: "))
    while number != 0:
        if number < 0:
            negative += 1
        number = int(input("Enter a number: "))
    print("Number of negative integers:", negative)

main()