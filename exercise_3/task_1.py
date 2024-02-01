# File: task_1.py
# Author: Kirill Nikolaev

# # a. Encapsulation in OOP: 
# Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP). 
# It refers to the bundling of data, and methods that operate on that data, 
# into a single unit known as a class. 
# This mechanism helps to hide the internal state of an object 
# and protect it from direct modification from outside the class, 
# providing a way to control access to the data.

from typing import List


class Prisoner:
    def __init__(self, name, status):
        self.name = name
        self.status = status

class Prison:
    def __init__(self):
        self.prisoners = []
        self.__amountOfPrisoners = len(self.prisoners)  # private attribute

    def add_prisoner(self, new_prisoners: List[Prisoner]):
        for prisoner in new_prisoners:
            if prisoner.status.lower() != "political":
                self.prisoners.append(prisoner)
            self.__amountOfPrisoners = len(self.prisoners)
        return self.__amountOfPrisoners # private attribute

    def release_prisoner(self, prisoners_to_release: List[Prisoner]):
        for prisoner in prisoners_to_release:
            if prisoner in self.prisoners and prisoner.status.lower() != "political":
                self.prisoners.remove(prisoner)
            self.__amountOfPrisoners = len(self.prisoners)
        return self.__amountOfPrisoners # private attribute
    
def main():
    prison = Prison()
    prisoners = [Prisoner("Navalny", "political"), Prisoner("Petrov", "criminal"), Prisoner("Sidorov", "criminal")]
    prison.add_prisoner(prisoners)
    print("Amount of prisoners: ", prison.add_prisoner(prisoners))
    print("Amount of prisoners: ", prison.release_prisoner(prisoners))

main()

# # b. Client in OOP: 
# In the context of OOP, a client is an entity that uses an object. 
# The client can be another object or a function. 
# The client interacts with the object through its methods (the object's public interface), 
# but does not have direct access to the object's data attributes due to encapsulation.

class Dog:
    def bark(self):
        return "Гав-гав!"

def main():
    my_dog = Dog()  # my_dog is an instance of Dog
    print(my_dog.bark())  # main function is the client of Dog class

main()

# # c. Data Attributes in OOP: 
# Data attributes, also known as instance variables or fields, 
# are the variables that hold data associated with an object. 
# They represent the state of an object. 
# Each instance of a class has its own set of data attributes. 
# For example, in a Person class, name and age could be data attributes.

class President:
    def __init__(self, values, experience, rating):
        self.values = values            # data attribute
        self.experience = experience    # data attribute
        self.rating = rating            # data attribute


# # d. Instance in OOP: 
# An instance in OOP refers to a specific object that is created from a class.  
# Each instance of a class has its own set of data attributes (state) 
# and can use the methods defined in the class.
        
class Cat:
    def __init__(self, name):
        self.name = name

fluffy = Cat("Fluffy")  # fluffy is an instance of Cat