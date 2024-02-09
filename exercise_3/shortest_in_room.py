# TEE RATKAISUSI TÄHÄN:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons) == 0
    
    def total_height(self):
        return sum(person.height for person in self.persons)

    def print_contents(self):
        if self.is_empty():
            print("The room is empty.")
        else:
            print(
                f"There are {len(self.persons)} persons in the room, "
                f"and their combined height is {self.total_height()} cm."
            )
            for person in self.persons:
                print(f"{person} ({person.height} cm)")

def main():
    room =Room()

    print("Is the room empty?",room.is_empty())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 175))

    print("Is the room empty?",room.is_empty())

    room.print_contents()

if __name__ == "__main__":
    main()