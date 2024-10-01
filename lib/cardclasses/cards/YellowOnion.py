from ..bases.minion import *

class YellowOnion(Minion):
    pass


def load_me():
    this_minion = YellowOnion(
        set = "1", # str
        number = 6, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Yellow Onion", # str
        image = "06_Yellow_Onion.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Passive"'], # list[str]
        base_attack = 0, # int
        base_health = 4, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = ['Gloom'], # list[str](optional)
        ability_descriptions = ['Onion'] # list[str](optional)
    )
    
    return this_minion