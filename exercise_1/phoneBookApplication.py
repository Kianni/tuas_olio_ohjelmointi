# File name: phoneBookApplication.py
# Author: Kirill
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

def work_with_phone_book(phone_book):
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            get_number(phone_book)
        elif command == 2:
            add_number(phone_book)
        elif command == 3:
            if quit():
                break
        else:
            print("Invalid command. Please enter 1, 2, or 3.")

def main():
    phone_book = {}
    work_with_phone_book(phone_book)
    
main()
