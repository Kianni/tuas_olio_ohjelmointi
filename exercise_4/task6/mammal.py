# File: mammal.py
# Author: Kirill Nikolaev
# Description: Mammal

class Mammal:
    def __init__(self, id, species, name, size, weight):
        self.__id = id
        self.__species = species
        self.__name = name
        self.__size = size
        self.__weight = weight

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, species):
        self.__species = species

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__weight = weight

    def __str__(self) -> str:
        return f"Mammal {self.__name} of species {self.__species} with id {self.__id}"
    
def main():
    mammal1 = Mammal(1, "Elephant", "Dumbo", 3.5, 5000)
    mammal2 = Mammal(2, "Giraffe", "Melman", 5.5, 1500)
    print(mammal1)
    print(mammal2)

if __name__ == "__main__":
    main()