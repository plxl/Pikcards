from ..bases.minion import *

class BurgeoningSpiderwort(Minion):
    pass


def load_me():
    this_minion = BurgeoningSpiderwort(
        set = "2", # str
        number = 8, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Burgeoning Spiderwort", # str
        image = "008_Burgeoning_Spiderwort.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive'], # list[str]
        base_attack = 0, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Fire', 'Mushroom'], # list[str](optional)
        ability_descriptions = ['Berry Boost'] # list[str](optional)
    )
    
    return this_minion