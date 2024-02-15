class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                #it is possible to first select some items from a list separately, 
                #and then take the rest of the items in a new list. 
                #https://programming-24.mooc.fi/part-6/1-reading-files#reading-csv-files
                name, *numbers = parts
                names[name] = numbers

        return names
    
    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")