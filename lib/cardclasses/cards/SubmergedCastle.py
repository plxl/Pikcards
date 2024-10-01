from ..bases.exploration import *

class SubmergedCastle(Exploration):
    pass


def load_me():
    this_exploration = SubmergedCastle(
        set = "2", # str
        number = 117, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Submerged Castle", # str
        image = "117_Submerged_Castle.png", # str
        cardclass = 3, # int
        base_energy = 1, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Submerged Castle'] # list[str](optional)
    )
    
    return this_exploration