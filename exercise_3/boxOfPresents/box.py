# File: box.py
# Author: Kirill Nikolaev
# Description: a box contains presents from present.py

from present import Present

class Box:
    def __init__(self):
        self.presents = []
        self._total_weight = 0

    def add_present(self, present: Present):
        self.presents.append(present)
        self._total_weight += present.weight

    def total_weight(self):
        return self._total_weight

def main():
    book = Present("Ta-Nehisi Coates:The Water Dancer",200)
    box = Box()
    box.add_present(book)

    print(box.total_weight())
    cd = Present("Pink Floyd: Dark Side of the Moon",50)
    box.add_present(cd)
    print(box.total_weight())
    
if __name__ == "__main__":
    main()