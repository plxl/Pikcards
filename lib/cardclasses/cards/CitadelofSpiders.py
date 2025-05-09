from ..bases.exploration import *

class CitadelofSpiders(Exploration):
    pass


def load_me():
    this_exploration = CitadelofSpiders(
        set = "2", # str
        number = 114, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Citadel of Spiders", # str
        image = "114_Citadel_of_Spiders.png", # str
        cardclass = 4, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Citadel of Spiders'] # list[str](optional)
    )
    
    return this_exploration