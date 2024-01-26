# File: pet.py
# Author: Kirill Nikolaev
# Description: as in task description

class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name: str, species: str, year_of_birth: int) -> Pet:
    return Pet(name, species, year_of_birth)

fluffy = new_pet('Fluffy', 'dog', 2017)

print(f"Name: {fluffy.name}, Species: {fluffy.species}, Year of birth: {fluffy.year_of_birth}")