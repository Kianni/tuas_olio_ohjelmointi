# File: phonebook.py
# Author: Kirill Nikolaev
# Description: Phonebook class

from person import Person

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        person = self.get_entry(name)
        if person == None:
            new_person = Person(name)
            new_person.add_number(number)
            self.__persons[name] = new_person
        else:
            person.add_number(number)

    def add_address(self, name: str, address: str):
        person = self.get_entry(name)
        if person == None:
            new_person = Person(name)
            new_person.add_address(address)
            self.__persons[name] = new_person
        else:
            person.add_address(address)
    
    def get_entry(self, name: str):
        if not name in self.__persons:
            return None

        return self.__persons[name]

    def get_numbers(self, name: str):
        person = self.get_entry(name)
        if person == None:
            return None

        return person.numbers()
    
    def get_address(self, name: str):
        person = self.get_entry(name)
        if person == None:
            return None

        return person.address()
    
def main():
    phonebook = PhoneBook()
    phonebook.add_number("Eric", "02-123456")
    print(phonebook.get_numbers("Eric"))
    print(phonebook.get_numbers("Emily"))
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Emily"))

if __name__ == "__main__":
    main()