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
    
    def mark_finished(self, id):
        for order in self.orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"No task with id {id} found")

    def finished_orders(self):
        return [order for order in self.orders if order.is_finished()]

    def unfinished_orders(self):
        return [order for order in self.orders if not order.is_finished()]

    def status_of_programmer(self, programmer):
        finished = [order for order in self.orders if order.programmer == programmer and order.is_finished()]
        unfinished = [order for order in self.orders if order.programmer == programmer and not order.is_finished()]

        finished_hours = sum(order.workload for order in finished)
        unfinished_hours = sum(order.workload for order in unfinished)

        return len(finished), finished_hours, len(unfinished), unfinished_hours
    
def main():
    orders=OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook","Eric",1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status=orders.status_of_programmer("Adele")
    print(status)

    for order in orders.all_orders():
        print(order)

    print()

    for programmer in orders.programmers():
        print(programmer)

if __name__ == "__main__":
    main()