# File: alarmClock.py
# Author: Kirill Nikolaev
# Description: simple alarm clock

import time
import os
import winsound

# ASCII art for digits and "alarm on" text
# Each digit is 5 characters wide and 5 lines tall
DIGITS = {
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
    ':': '     \n  ** \n     \n  ** \n     ',
    'A': '  A  \n A A \nA   A\nAAAAA\nA   A',
    'L': 'L    \nL    \nL    \nL    \nLLLLL',
    'R': 'RRRR \nR   R\nRRRR \nR R  \nR  RR',
    'M': 'M   M\nMM MM\nM M M\nM   M\nM   M',
    'O': ' OOO \nO   O\nO   O\nO   O\n OOO ',
    'N': 'N   N\nNN  N\nN N N\nN  NN\nN   N',
    ' ': '     \n     \n     \n     \n     '
}

ASCII_LINES = 5

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
    
    # Private method
    def _check_alarm(self):
        if (self.alarm_hours is not None and self.hours >= self.alarm_hours and
            self.alarm_minutes is not None and self.minutes >= self.alarm_minutes and
            self.alarm_seconds is not None and self.seconds >= self.alarm_seconds):
            self.alarm_on = True

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
        self._check_alarm()
    
    # Private method
    def _generate_ascii_art(self, string): 
        lines = ['' for _ in range(ASCII_LINES)]                # initialize 5 empty strings in a list    
        for char in string:                                     # iterate over each character in time_string 
            for i, line in enumerate(DIGITS[char].split('\n')): # take each line of the digit and enumerate it
                lines[i] += line + '  '                         # put each line of the digit into the corresponding line of the output
        return lines
    
    def display_time(self):

        # Check if alarm is on and current second is divisible by 3
        if self.alarm_on and self.seconds % 3 == 0:
            time_string = "ALARM ON"
            winsound.MessageBeep(winsound.MB_ICONHAND)  # play "critical stop" sound
        else:
            time_string = f"{str(self.hours).zfill(2)}:{str(self.minutes).zfill(2)}:{str(self.seconds).zfill(2)}"

        # Convert time string to ASCII art
        lines = self._generate_ascii_art(time_string)

        # Insert ANSI escape codes into ASCII art
        for i in range(len(lines)):
            if self.alarm_on:
                lines[i] = '\033[91m' + lines[i] + '\033[0m'  # Red for alarm
            else:
                lines[i] = '\033[92m' + lines[i] + '\033[0m'  # Green for normal time

        return '\n'.join(lines)

def main():
    my_clock = Clock(10, 30, 45)
    my_clock.set_alarm(10, 30, 50)

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(my_clock.display_time())
        time.sleep(1)
        my_clock.tick()

main()

