# File: person.py
# Author: Kirill Nikolaev
# Description: Person class

class Person:
    def __init__(self, name):
        self._name = name
        self._numbers = []
        self._address = None

    def name(self):
        return self._name

    def numbers(self):
        return self._numbers

    def address(self):
        return self._address

    def add_number(self, number):
        self._numbers.append(number)

    def add_address(self, address):
        self._address = address

    def __str__(self):
        return self._name

def main():
    person=Person("Eric")
    print(person.name())
    print(person.numbers())
    print(person.address())
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers())
    print(person.address())

if __name__ == "__main__":
    main()