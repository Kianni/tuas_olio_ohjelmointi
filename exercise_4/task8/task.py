# File: task.py
# Author: Kirill Nikolaev
# Description: Task class

class Task:
    id_counter = 1

    def __init__(self, description, programmer, workload):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def __str__(self):
        status = "FINISHED" if self.finished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

    def is_finished(self):
        return self.finished

    def mark_finished(self):
        self.finished = True

def main():
    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload)
    print(t1)
    print(t1.is_finished())
    t1.mark_finished()
    print(t1)
    print(t1.is_finished())
    t2=Task("program webstore", "Adele", 10)
    t3=Task("program mobile app for workload accounting", "Eric", 25)
    print(t2)
    print(t3)

if __name__ == "__main__":
    main()