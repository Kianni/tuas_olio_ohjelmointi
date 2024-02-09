# File: present.py
# Author: Kirill Nikolaev
# Description: a present has anameand a weight

class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight}g)"

def main():
    book =Present("Ta-Nehisi Coates: The Water Dancer", 200)
    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:",book)
    
if __name__ == "__main__":
    main()