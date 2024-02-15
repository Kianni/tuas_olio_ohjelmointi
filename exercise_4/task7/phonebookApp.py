# File: phonebook.py
# Author: Kirill Nikolaev
# Description: Phonebook application

from phonebook import PhoneBook

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 add address")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        person = self.__phonebook.add_address(name, address)

    def print_numbers(self, name):
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None or len(numbers) == 0:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def print_address(self, name):
        address = self.__phonebook.get_address(name)
        if address == None:
            print("address unknown")
            return
        print(address)
    
    def search(self):
        name = input("name: ")
        self.print_numbers(name)
        self.print_address(name)        

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

def main():
    application = PhoneBookApplication()
    application.execute()

if __name__ == "__main__":
    main()