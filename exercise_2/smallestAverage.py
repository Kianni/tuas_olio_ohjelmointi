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
def smallestAverage(contestant1, contestant2, contestant3):
    # calculate average for each contestant
    contestant1Average = countAverage(contestant1)
    contestant2Average = countAverage(contestant2)
    contestant3Average = countAverage(contestant3)

    # compare averages
    if contestant1Average < contestant2Average and contestant1Average < contestant3Average:
        return contestant1
    elif contestant2Average < contestant1Average and contestant2Average < contestant3Average:
        return contestant2
    else:
        return contestant3
    

# print result
print(smallestAverage(contestant1, contestant2, contestant3))

