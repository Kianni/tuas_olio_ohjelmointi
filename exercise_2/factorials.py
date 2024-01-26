# File: factorials.py
# Author: Kirill Nikolaev
# Description: returns the factorials of the numbers 1 to n in a dictionary

def calculate_factorial(i):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    return factorial

def factorials(n):
    factorialsForEachNumber = {}

    for i in range(1, n + 1):
        factorialsForEachNumber[i] = calculate_factorial(i)
        
    return factorialsForEachNumber

k = factorials(5)
print(k[1])
print(k[3])
print(k[5])