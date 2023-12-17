import random
from abc import ABC, abstractmethod


class Elf(ABC):

    def __init__(self, name, mus_instrument, favorite_song):
        self.name = name
        self.mus_instrument = mus_instrument
        self.favorite_song = favorite_song

    def play_song(self):
        print(f"Elf {self.name} playing {self.favorite_song} "
              f"on {self.mus_instrument}")
    @abstractmethod
    def song_battle(self):
        pass

    @abstractmethod
    def fight(self):
        pass


class ElfRanger(Elf):

    def __init__(self, name, mus_instrument, favorite_song, bow: dict):
        super().__init__(name, mus_instrument, favorite_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def song_battle(self):
        print(f"Elf {self.name} plays the {self.mus_instrument} and gets a rating of {random.randint(1,10)}/10.")
    def fight(self):
        opponents = ["John","Sandy"]
        print(f"Elf {self.name} kills {random.choice(opponents)} with {self.bow}")

class MoonElf(Elf):
    def __init__(self, name, mus_instrument, favorite_song, bow: dict):
        super().__init__(name, mus_instrument, favorite_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]


    def song_battle(self):
        print(f"Elf {self.name} plays the {self.mus_instrument} and gets a rating of {random.randint(1,10)}/10.")

    def fight(self):
        opponents = ["Bob", "Sandy"]
        print(f"Elf {self.name} kills {random.choice(opponents)} with {self.bow}")

class SandElf(Elf):
    def __init__(self, name, mus_instrument, favorite_song, bow: dict):
        super().__init__(name, mus_instrument, favorite_song)
        self.damage = bow["damage"]
        self.bow = bow["name"]

    def song_battle(self):

        print(f"Elf {self.name} plays the {self.mus_instrument} and gets a rating of {random.randint(1,10)}/10.")

    def fight(self):
        opponents = ["John", "Bob"]
        print(f"Elf {self.name} kills {random.choice(opponents)} with {self.bow}")

bob = ElfRanger("Bob",
                "lute",
                "Bad Romance",
                {"name": "M249", "damage": 999})

john = MoonElf("John",
                "harp",
                "Good Romance",
                {"name": "M350", "damage": 1050})

sandy = SandElf("Sandy",
                "flute",
                "Cheerful Romance",
                {"name": "M350", "damage": 970})
def playing_song():
    bob.play_song()
    john.play_song()
    sandy.play_song()
def fight():
    bob.fight()
    john.fight()
    sandy.fight()
def song_battle():
    bob.song_battle()
    john.song_battle()
    sandy.song_battle()

playing_song()
fight()
song_battle()

