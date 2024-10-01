from ..bases.area import *

class ScaleBlocks(Area):
    pass


def load_me():
    this_area = ScaleBlocks(
        set = "C", # str
        number = 32, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Scale Blocks", # str
        image = "32_Scale_Blocks.png", # str
        cardclass = 5, # int
        base_energy = 2, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Scale Blocks'] # list[str](optional)
    )
    
    return this_area