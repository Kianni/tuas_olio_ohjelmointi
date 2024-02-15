# File: orderBook.py
# Author: Kirill Nikolaev
# Description: orderBook class

from task import Task

class OrderBook:
    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([order.programmer for order in self.orders]))
    
def main():
    orders=OrderBook()
    orders.add_order("program webstore","Adele",10)
    orders.add_order("program mobile app for workload accounting","Eric",25)
    orders.add_order("program app for practising mathematics","Adele",100)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

if __name__ == "__main__":
    main()