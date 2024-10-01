from ..bases.minion import *

class PurplePikmin(Minion):
    pass


def load_me():
    this_minion = PurplePikmin(
        set = "2", # str
        number = 3, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Purple Pikmin", # str
        image = "003_Purple_Pikmin.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Pikmin"'], # list[str]
        base_attack = 2, # int
        base_health = 1, # int
        defense = 0, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Thud Entrance', 'Steady Feet'] # list[str](optional)
    )
    
    return this_minion