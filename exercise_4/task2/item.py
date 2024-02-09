# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: Item

class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight}g)"
    
def main():
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())
    print("Book:", book)
    print("Phone:", phone)

    # book.weight=100 # add a new attribute to the class and rewrite method weight!
    # print("Weight of the book:", book.weight())
    book._Item__weight = 777 # double underscore means 'name mangling'
    print("Weight of the book:", book.weight())

if __name__ == "__main__":
    main()