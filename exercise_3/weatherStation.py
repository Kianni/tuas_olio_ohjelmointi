# File: weatherStation.py
# Author: Kirill Nikolaev
# Description: a class named WeatherStationwhich is used to store observations about the weather.

class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = []

    def add_observation(self, observation: str):
        self.__observations.append(observation)

    def latest_observation(self) -> str: #hint on type of return value
        return self.__observations[-1] if self.__observations else ''

    def number_of_observations(self) -> int: #hint on type of return value
        return len(self.__observations)

    def __str__(self) -> str: #hint on type of return value
        return f'{self.__name}, {self.number_of_observations()} observations'
    
def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())
    station.add_observation("Thunderstorm")
    print(station.latest_observation())
    print(station.number_of_observations())
    print(station)

if __name__ == "__main__":
    main()