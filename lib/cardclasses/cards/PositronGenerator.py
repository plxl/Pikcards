from ..bases.item import *

class PositronGenerator(Item):
    pass


def load_me():
    this_item = PositronGenerator(
        set = "1", # str
        number = 62, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Positron Generator", # str
        image = "62_Positron_Generator.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Dolphin Part"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Convert to Energy'] # list[str](optional)
    )
    
    return this_item