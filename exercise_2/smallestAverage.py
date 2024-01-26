# File: factorials.py
# Author: Kirill Nikolaev
# Description: takes three contestants profile and 
# returns the contestant profile which contains the smallest average from three result values

# contestant profile
# name: string
# result1: int
# result2: int
# result3: int

contestant1 = {
    'name': 'Kirill',
    'result1': 10,
    'result2': 20,
    'result3': 30
}

contestant2 = {
    'name': 'Mike',
    'result1': 1,
    'result2': 2,
    'result3': 3
}

contestant3 = {
    'name': 'Artjom',
    'result1': 100,
    'result2': 200,
    'result3': 300
}

def countAverage(contestant):
    return (contestant['result1'] + contestant['result2'] + contestant['result3']) / 3

# returns the contestant profile which contains the smallest average from three result values
def smallestAverage(contestants):
    # Use the built-in min function with a custom key function
    return min(contestants, key=countAverage)
    

# print result
print(smallestAverage([contestant1, contestant2, contestant3]))

