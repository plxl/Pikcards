from ..bases.item import *

class IndustrialSet(Item):
    pass


def load_me():
    this_item = IndustrialSet(
        set = "2", # str
        number = 67, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Industrial Set", # str
        image = "067_Industrial_Set.png", # str
        cardclass = 3, # int
        base_energy = 4, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"2 Defense"', '"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item