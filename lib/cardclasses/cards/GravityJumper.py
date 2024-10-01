from ..bases.item import *

class GravityJumper(Item):
    pass


def load_me():
    this_item = GravityJumper(
        set = "1", # str
        number = 51, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Gravity Jumper", # str
        image = "51_Gravity_Jumper.png", # str
        cardclass = 2, # int
        base_energy = 2, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Dolphin Part"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Return'] # list[str](optional)
    )
    
    return this_item