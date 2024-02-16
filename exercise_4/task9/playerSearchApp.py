# File: playerSearchApp.py
# Author: Kirill Nikolaev
# Description: playerSearchApp class

import json

class HockeyStats:
    def __init__(self, filename):
        self.data = self.load_data(filename)

    def search_for_player(self, name):
        for player in self.data:
            if player['name'] == name:
                print(f"{name:<20} {player['team']:>3} {player['goals']:>2} + {player['assists']:>2} = {player['goals'] + player['assists']:>2}")

    def list_teams(self):
        teams = sorted(set(player['team'] for player in self.data))
        print('\n'.join(teams))

    def list_countries(self):
        countries = sorted(set(player['nationality'] for player in self.data))
        print('\n'.join(countries))

    def load_data(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"read the data of {len(data)} players")
        return data
        
    def main(self):
        while True:
            print("commands:")
            print("0 quit")
            print("1 search for player")
            print("2 teams")
            print("3 countries")
            print("4 players in team")
            print("5 players from country")
            print("6 most points")
            print("7 most goals")
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                name = input("name: ")
                self.search_for_player(name)
            elif command == 2:
                self.list_teams()
            elif command == 3:
                self.list_countries()

def main():
    filename = input("file name: ")
    stats = HockeyStats(filename)
    stats.main()

if __name__ == "__main__":
    main()