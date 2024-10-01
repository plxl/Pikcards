from ..bases.exploration import *

class PikminFinder(Exploration):
    pass


def load_me():
    this_exploration = PikminFinder(
        set = "C", # str
        number = 37, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Pikmin Finder", # str
        image = "37_Pikmin_Finder.png", # str
        cardclass = 5, # int
        base_energy = 2, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Pikmin Finder'] # list[str](optional)
    )
    
    return this_exploration