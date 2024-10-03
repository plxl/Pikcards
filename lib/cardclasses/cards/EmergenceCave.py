from ..bases.exploration import *

class EmergenceCave(Exploration):
    pass


def load_me():
    this_exploration = EmergenceCave(
        set = "2", # str
        number = 107, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Emergence Cave", # str
        image = "107_Emergence_Cave.png", # str
        cardclass = 2, # int
        base_energy = 1, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Emergence Cave'] # list[str](optional)
    )
    
    return this_exploration