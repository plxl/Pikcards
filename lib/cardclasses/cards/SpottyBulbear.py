from ..bases.minion import *

class SpottyBulbear(Minion):
    pass


def load_me():
    this_minion = SpottyBulbear(
        set = "1", # str
        number = 14, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Spotty Bulbear", # str
        image = "14_Spotty_Bulbear.png", # str
        cardclass = 1, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ["GrubDog"], # list[str]
        base_attack = 5, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_minion