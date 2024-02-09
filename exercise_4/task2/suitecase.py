# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: Suitecase

from item import Item

class Suitcase:
    def __init__(self, max_weight):
        self._items = []
        self._max_weight = max_weight

    def add_item(self, item):
        if item.weight() + sum(i.weight() for i in self._items) <= self._max_weight:
            self._items.append(item)
    
    def print_items(self):
        for item in self._items:
            print(item)
    
    def weight(self):
        return sum(item.weight() for item in self._items)
    
    def heaviest_item(self):
        if not self._items:
            return None
        return max(self._items, key=lambda item: item.weight())

    def __str__(self):
        total_weight = sum(item.weight() for item in self._items)
        return (f"{len(self._items)} "
                f"{'item' if len(self._items) == 1 else 'items'} "
                f"({total_weight}g)")
    
def main():
    book = Item("ABC Book", 200)
    phone = Item("Nokia 3210", 100)
    brick = Item("Brick", 400)

    suitcase = Suitcase(1000)

    print(suitcase)

    suitcase.add_item(book)
    print(suitcase)

    suitcase.add_item(phone)
    print(suitcase)

    suitcase.add_item(brick)
    print(suitcase)

    #part 4
    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight}g")

    # part 5
    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")

if __name__ == "__main__":
    main()