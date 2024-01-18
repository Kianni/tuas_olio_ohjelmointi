# File name: phoneBookApplication.py
# Author: Kirill
# Description: user can add and search phone numbers using the console

def main():
    phone_book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit): "))
        if command == 1:
            name = input("name: ")
            print(phone_book.get(name, "no number"))
        elif command == 2:
            name = input("name: ")
            number = input("number: ")
            phone_book[name] = number
            print("ok!")
        elif command == 3:
            print("quitting...")
            break
        else:
            print("Invalid command. Please enter 1, 2, or 3.")

main()
