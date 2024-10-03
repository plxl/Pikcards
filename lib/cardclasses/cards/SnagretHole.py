from ..bases.exploration import *

class SnagretHole(Exploration):
    pass


def load_me():
    this_exploration = SnagretHole(
        set = "2", # str
        number = 113, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Snagret Hole", # str
        image = "113_Snagret_Hole.png", # str
        cardclass = 2, # int
        base_energy = 0, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Snagret Hole'] # list[str](optional)
    )
    
    return this_exploration