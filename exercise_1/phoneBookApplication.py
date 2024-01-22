# File name: phoneBookApplication.py
# Author: Kirill Nikolaev
# Description: user can add and search phone numbers using the console

def get_number(phone_book):
    name = input("name: ")
    print(phone_book.get(name, "no number"))

def add_number(phone_book):
    name = input("name: ")
    number = input("number: ")
    phone_book[name] = number
    print("ok!")

def quit():
    print("quitting...")
    return True

def invalid_command():
    print("Invalid command. Please enter 1, 2, or 3.")

def work_with_phone_book(phone_book):
    commands = {1: get_number, 2: add_number, 3: quit, 'default': invalid_command}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        action = commands.get(command, commands['default'])
        if action == quit and action():
            break
        else:
            action(phone_book)

def main():
    phone_book = {}
    work_with_phone_book(phone_book)

main()
