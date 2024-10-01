from ..bases.exploration import *

class WhiteFlowerGarden(Exploration):
    pass


def load_me():
    this_exploration = WhiteFlowerGarden(
        set = "2", # str
        number = 111, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "White Flower Garden", # str
        image = "111_White_Flower_Garden.png", # str
        cardclass = 2, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['White Flower Garden'] # list[str](optional)
    )
    
    return this_exploration