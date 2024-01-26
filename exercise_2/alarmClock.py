# File: alarmClock.py
# Author: Kirill Nikolaev
# Description: simple alarm clock

import time
import os

class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.alarm_hours = None
        self.alarm_minutes = None
        self.alarm_seconds = None
        self.alarm_on = False

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
    
            # Check if alarm should be on
        if (self.alarm_hours is not None and self.hours >= self.alarm_hours and
            self.alarm_minutes is not None and self.minutes >= self.alarm_minutes and
            self.alarm_seconds is not None and self.seconds >= self.alarm_seconds):
            self.alarm_on = True
    
    def display_time(self):
        digits = {
            '0': ' 000 \n0   0\n0   0\n0   0\n 000 ',
            '1': '  1  \n 11  \n  1  \n  1  \n11111',
            '2': ' 222 \n    2\n  22 \n 2   \n22222',
            '3': '3333 \n    3\n 333 \n    3\n3333 ',
            '4': '4   4\n4   4\n44444\n    4\n    4',
            '5': '55555\n5    \n5555 \n    5\n5555 ',
            '6': ' 666 \n6    \n6666 \n6   6\n 666 ',
            '7': '77777\n   7 \n  7  \n 7   \n7    ',
            '8': ' 888 \n8   8\n 888 \n8   8\n 888 ',
            '9': ' 999\n9   9\n 9999\n    9\n 999 ',
            ':': '     \n  ** \n     \n  ** \n     '
        }

        time_string = f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

        # Convert time string to ASCII art
        lines = ['' for _ in range(5)]                          # initialize 5 empty strings in a list
        for char in time_string:                                # iterate over each character in time_string          
            for i, line in enumerate(digits[char].split('\n')): # take each line of the digit and enumerate it
                lines[i] += line + '  '                         # put each line of the digit into the corresponding line of the output

        # Insert ANSI escape codes into ASCII art
        for i in range(len(lines)):
            if self.alarm_on:
                lines[i] = '\033[91m' + lines[i] + '\033[0m'  # Red for alarm
            else:
                lines[i] = '\033[92m' + lines[i] + '\033[0m'  # Green for normal time

        return '\n'.join(lines)



my_clock = Clock(10, 30, 45)
my_clock.set_alarm(10, 30, 50)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(my_clock.display_time())
    time.sleep(1)
    my_clock.tick()