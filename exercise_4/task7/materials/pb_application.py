from phonebook import PhoneBook
from file_handler import FileHandler

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("Lecture 6\phonebook\phonebook.txt")

        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def search_by_number(self):
        number = input("number: ")
        name = self.__phonebook.number_search(number)
        if name == None:
            print("unknown number")
        else:
            print(name)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_by_number()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()