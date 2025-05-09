from ..bases.exploration import *

class GluttonsKitchen(Exploration):
    pass


def load_me():
    this_exploration = GluttonsKitchen(
        set = "2", # str
        number = 115, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Glutton's Kitchen", # str
        image = "115_Glutton's_Kitchen.png", # str
        cardclass = 4, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ["Glutton's Kitchen"] # list[str](optional)
    )
    
    return this_exploration