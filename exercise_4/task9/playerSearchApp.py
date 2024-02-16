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
    
    def format_player(self, player):
        return (
            f"{player['name']:<20} "
            f"{player['team']:>3} "
            f"{player['goals']:>2} + "
            f"{player['assists']:>2} = "
            f"{player['goals'] + player['assists']:>2}"
        )
    
    def get_score(self, player):
        return player['goals'] + player['assists']

    def list_players_in_team(self, team):
        players = [player for player in self.data if player['team'] == team]
        players.sort(key=lambda player: self.get_score(player), reverse=True)
        for player in players:
            print(self.format_player(player))

    def list_players_from_country(self, country):
        players = [player for player in self.data if player['nationality'] == country]
        players.sort(key=lambda player: self.get_score(player), reverse=True)
        for player in players:
            print(self.format_player(player))

    def most_points(self, n):
        players = sorted(self.data, key=lambda player: (self.get_score(player), player['goals']), reverse=True)
        for player in players[:n]:
            print(self.format_player(player))

    def most_goals(self, n):
        players = sorted(self.data, key=lambda player: (player['goals'], -player['games']), reverse=True)
        for player in players[:n]:
            print(self.format_player(player))
    
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
            elif command == 4:
                team = input("team: ")
                self.list_players_in_team(team)
            elif command == 5:
                country = input("country: ")
                self.list_players_from_country(country)
            elif command == 6:
                n = int(input("how many: "))
                self.most_points(n)
            elif command == 7:
                n = int(input("how many: "))
                self.most_goals(n)

def main():
    filename = input("file name: ")
    stats = HockeyStats(filename)
    stats.main()

if __name__ == "__main__":
    main()