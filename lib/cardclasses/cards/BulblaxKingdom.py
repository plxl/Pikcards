from ..bases.exploration import *

class BulblaxKingdom(Exploration):
    pass


def load_me():
    this_exploration = BulblaxKingdom(
        set = "2", # str
        number = 112, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Bulblax Kingdom", # str
        image = "112_Bulblax_Kingdom.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Bulblax Kingdom'] # list[str](optional)
    )
    
    return this_exploration