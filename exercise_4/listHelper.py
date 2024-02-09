# File: serviceCharge.py
# Author: Kirill Nikolaev
# Description: a class named ListHelper which contains two class methods

class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        if not my_list:
            return None
        max_count = 0
        max_item = my_list[0]
        for item in my_list:
            item_count = my_list.count(item)
            if item_count > max_count:
                max_count = item_count
                max_item = item
        return max_item

    @classmethod
    def doubles(cls, my_list: list):
        if not my_list:
            return 0
        unique_items = set(my_list)
        return sum(1 for item in unique_items if my_list.count(item) >= 2)
    
def main():
    numbers =[1,1,2,1,3,3,4,5,5,5,6,5,5,5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

if __name__ == "__main__":
    main()