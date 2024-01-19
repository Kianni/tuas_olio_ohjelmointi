# File name: arithmeticProgression.py
# Author: Kirill
# Description: takes the maximum value of the progression from the user
# counts the number of terms that appeared in the AP, 
# the sum of the terms and the sum of the squared terms

def print_progression(max_value):
    if max_value < 3:
        print("Procession is: ")
    else:
        progression = [str(i) for i in range(3, max_value + 1, 3)]
        print("Procession is: " + ", ".join(progression))

def print_to_console(max_value, sum, sum_squares, count):
    print_progression(max_value)
    print("Number of terms:", count)
    print("Sum of terms is:", sum)
    print("Sum of squared terms is:", sum_squares)

def build_progression(max_value):
    sum = 0
    sum_squares = 0
    count = 0
    for i in range(3, max_value + 1, 3):
        sum += i
        sum_squares += i ** 2
        count += 1
    return sum, sum_squares, count

def main():
    max_value = int(input("Give maximum value: "))
    sum, sum_squares, count = build_progression(max_value)
    print_to_console(max_value, sum, sum_squares, count)

main()
