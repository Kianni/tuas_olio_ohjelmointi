# File: alarmClock.py
# Author: Kirill Nikolaev
# Description: simple alarm clock

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def display_time(self):
        return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"


# Usage
my_clock = Clock(10, 30, 45)
print(my_clock.display_time())  # prints: 10:30:45
my_clock.tick()
print(my_clock.display_time())  # prints: 10:30:46