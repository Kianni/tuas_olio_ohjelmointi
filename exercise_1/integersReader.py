# File name: integersReader.py
# Author: Kirill
# Description: repeatedly reads integers until the user enters 0. Print out the number of negative integers

def ask_for_number():
    return int(input("Enter a number: "))

def print_results(negative, even, sum_divisible_by_three):
    print("Number of negative integers:", negative)
    print("Number of even integers:", even)
    print("Sum of positive integers divisible by three:", sum_divisible_by_three)

def process_number(number, counters):
    if number < 0:
        counters['negative'] += 1
    if number % 2 == 0:
        counters['even'] += 1
    if number > 0 and number % 3 == 0:
        counters['sum_divisible_by_three'] += number
    return counters

def iterate_processing_numbers(counters):
    number = ask_for_number()
    while number != 0:
        counters = process_number(number, counters)
        number = ask_for_number()
    return counters

def main():
    counters = {'negative': 0, 'even': 0, 'sum_divisible_by_three': 0}
    counters = iterate_processing_numbers(counters)
    print_results(counters['negative'], counters['even'], counters['sum_divisible_by_three'])


main()