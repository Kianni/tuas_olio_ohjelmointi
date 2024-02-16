# File: orderBookApp.py
# Author: Kirill Nikolaev
# Description: orderBookApp class

from orderBook import OrderBook

class OrderBookApplication:
    def __init__(self):
        self.__orders = OrderBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()
        self.__orders.add_order(description, programmer, int(workload))
        print("added!")

    def list_finished_tasks(self):
        finished = self.__orders.finished_orders()
        if finished:
            for order in finished:
                print(order)
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        for order in self.__orders.unfinished_orders():
            print(order)

    def mark_task_as_finished(self):
        id = int(input("id: "))
        self.__orders.mark_finished(id)
        print("marked as finished")

    def programmers(self):
        for programmer in self.__orders.programmers():
            print(programmer)

    def status_of_programmer(self):
        programmer = input("programmer: ")
        finished, finished_hours, unfinished, unfinished_hours = self.__orders.status_of_programmer(programmer)
        print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_hours} scheduled {unfinished_hours}")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_task_as_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()

def main():
    application = OrderBookApplication()
    application.execute()

if __name__ == "__main__":
    main()