from ..bases.exploration import *

class PikminSpaceForce(Exploration):
    pass


def load_me():
    this_exploration = PikminSpaceForce(
        set = "C", # str
        number = 38, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Pikmin Space Force", # str
        image = "38_Pikmin_Space_Force.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Unknown Gameplay'] # list[str](optional)
    )
    
    return this_exploration