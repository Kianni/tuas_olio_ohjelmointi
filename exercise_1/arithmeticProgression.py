# File name: arithmeticProgression.py
# Author: Kirill
# Description: takes the maximum value of the progression from the user
# counts the number of terms that appeared in the AP, 
# the sum of the terms and the sum of the squared terms

def main():
    max_value = int(input("Enter the maximum value of the progression: "))
    sum = 0
    sum_squares = 0
    count = 0
    for i in range(3, max_value + 1, 3):
        sum += i
        sum_squares += i ** 2
        count += 1
    print("Number of terms:", count)
    print("Sum of terms:", sum)
    print("Sum of squares of terms:", sum_squares)

main()
