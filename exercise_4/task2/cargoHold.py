# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: CargoHold

from item import Item
from suitcase import Suitcase

class CargoHold:
    def __init__(self, max_weight):
        self._suitcases = []
        self._max_weight = max_weight*1000

    def add_suitcase(self, suitcase):
        if suitcase.weight() + self.total_weight() <= self._max_weight:
            self._suitcases.append(suitcase)

    def total_weight(self):
        return sum(suitcase.weight() for suitcase in self._suitcases)

    def __str__(self):
        remaining_weight = self._max_weight - self.total_weight()
        return (f"{len(self._suitcases)} " 
                f"{'suitcase' if len(self._suitcases) == 1 else 'suitcases'}, " 
                f"space for {remaining_weight/1000:.1f} kg")
    
def main():
    cargo_hold=CargoHold(100)
    print(cargo_hold)

    book = Item("ABC Book",200)
    phone = Item("Nokia 3210",100)
    brick = Item("Brick",400)

    adas_suitcase = Suitcase(1000)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(1000)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)
    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)

if __name__ == "__main__":
    main()