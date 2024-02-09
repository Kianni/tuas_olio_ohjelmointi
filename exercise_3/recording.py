# File: recording.py
# Author: Kirill Nikolaev
# Description: a class named Recording which models a single recording

class Recording:
    def __init__(self, length: int):
        self.__length = length

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    """
    def get_length(self):
        return self.__length

    def set_length(self, length: int):
        self.__length = length
    """

def main():
    the_hurriganes_live = Recording(43)
    print(the_hurriganes_live.length)
    the_hurriganes_live.length = 44
    print(the_hurriganes_live.length)

    """
    the_hurriganes_live = Recording(43)
    print(the_hurriganes_live.get_length())
    the_hurriganes_live.set_length(44)
    print(the_hurriganes_live.get_length())
    """

if __name__ == "__main__":
    main()