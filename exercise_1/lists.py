# File name: lists.py
# Author: Kirill
# Description: list 13 items and fill it with numbers asked from user, print the list out
# Description: list 13 items and fill it with strings asked from user, print the list out
# Description: fill the number list with randomly generated numbers and print it out

#Code a list of at least 10 items and fill it with numbers asked from user.
numbers = []
for i in range(13):
    number = int(input("Enter a number: "))
    numbers.append(number)
print(numbers)

#Do the same with strings. Print out both lists. 
strings = []
for i in range(13):
    string = input("Enter a string: ")
    strings.append(string)
print(strings)

#Then fill the number list with randomly generated numbers and print it out. 
import random
numbers = []
for i in range(13):
    number = random.randint(0,100)
    numbers.append(number)
print(numbers)

# Arrange numbers in the list from smallest to largest and strings in alphabetical order and print out the lists.
numbers.sort()
strings.sort()
print(numbers)
print(strings)
 
