# File: orderBookApp.py
# Author: Kirill Nikolaev
# Description: orderBookApp

from orderBook import OrderBook

def main():
    orders = OrderBook()
    commands = {
        "0": "exit",
        "1": "add order",
        "2": "list finished tasks",
        "3": "list unfinished tasks",
        "4": "mark task as finished",
        "5": "programmers",
        "6": "status of programmer"
    }

    while True:
        print("commands:")
        for key, value in commands.items():
            print(f"{key} {value}")
        command = input("command: ")

        if command == "0":
            break
        elif command == "1":
            description = input("description: ")
            programmer, workload = input("programmer and workload estimate: ").split()
            orders.add_order(description, programmer, int(workload))
            print("added!")
        elif command == "2":
            finished = orders.finished_orders()
            if finished:
                for order in finished:
                    print(order)
            else:
                print("no finished tasks")
        elif command == "3":
            for order in orders.unfinished_orders():
                print(order)
        elif command == "4":
            id = int(input("id: "))
            orders.mark_finished(id)
            print("marked as finished")
        elif command == "5":
            for programmer in orders.programmers():
                print(programmer)
        elif command == "6":
            programmer = input("programmer: ")
            finished, finished_hours, unfinished, unfinished_hours = orders.status_of_programmer(programmer)
            print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_hours} scheduled {unfinished_hours}")

if __name__ == "__main__":
    main()