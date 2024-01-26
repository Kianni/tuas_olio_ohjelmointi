# File: favoriteFiction.py
# Author: Kirill Nikolaev
# Description: as in task description

class Media:
    def __init__(self, name: str, creator: str, genre: str, year: int):
        self.name = name
        self.creator = creator
        self.genre = genre
        self.year = year

class Book(Media):
    pass

class Manga(Media):
    pass

class Anime(Media):
    pass

class Movie(Media):
    pass

class Song(Media):
    pass

mahabharata = Book('Mahabharata', 'Vyasa', 'Epic', 400)
print(f"Name: {mahabharata.name}, Creator: {mahabharata.creator}, Genre: {mahabharata.genre}, Year: {mahabharata.year}")

naruto = Manga('Naruto', 'Masashi Kishimoto', 'Shonen', 1999)
print(f"Name: {naruto.name}, Creator: {naruto.creator}, Genre: {naruto.genre}, Year: {naruto.year}")

deathNote = Anime('Death Note', 'Tsugumi Ohba', 'Shonen', 2003)
print(f"Name: {deathNote.name}, Creator: {deathNote.creator}, Genre: {deathNote.genre}, Year: {deathNote.year}")

theGodfather = Movie('The Godfather', 'Francis Ford Coppola', 'Crime', 1972)
print(f"Name: {theGodfather.name}, Creator: {theGodfather.creator}, Genre: {theGodfather.genre}, Year: {theGodfather.year}")

bohemianRhapsody = Song('Bohemian Rhapsody', 'Queen', 'Rock', 1975)
print(f"Name: {bohemianRhapsody.name}, Creator: {bohemianRhapsody.creator}, Genre: {bohemianRhapsody.genre}, Year: {bohemianRhapsody.year}")

