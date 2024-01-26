# File: alarmClock.py
# Author: Kirill Nikolaev
# Description: simple alarm clock

import time

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.alarm_hours = None
        self.alarm_minutes = None
        self.alarm_seconds = None

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_alarm(self, hours, minutes, seconds):
        self.alarm_hours = hours
        self.alarm_minutes = minutes
        self.alarm_seconds = seconds

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
        if (self.alarm_hours is not None and self.hours >= self.alarm_hours and
            self.alarm_minutes is not None and self.minutes >= self.alarm_minutes and
            self.alarm_seconds is not None and self.seconds >= self.alarm_seconds):
            return f"\033[91m{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}\033[0m"
        else:
            return f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"



my_clock = Clock(10, 30, 45)
my_clock.set_alarm(10, 31, 0)

while True:
    print(my_clock.display_time(), end='\r')
    time.sleep(1)
    my_clock.tick()