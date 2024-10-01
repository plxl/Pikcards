from ..bases.item import *

class SweetToothSeries(Item):
    pass


def load_me():
    this_item = SweetToothSeries(
        set = "2", # str
        number = 59, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Sweet Tooth Series", # str
        image = "059_Sweet_Tooth_Series.png", # str
        cardclass = 3, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = ['"Piercing"', '"Ice"'], # list[str]
        immunities = ['"Piercing"', '"Ice"'], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = ['Mushroom'], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item