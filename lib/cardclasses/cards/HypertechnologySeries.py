from ..bases.item import *

class HypertechnologySeries(Item):
    pass


def load_me():
    this_item = HypertechnologySeries(
        set = "2", # str
        number = 66, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Hyper-technology Series", # str
        image = "066_Hyper-technology_Series.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = ['Electricity'], # list[str]
        immunities = ['Electricity'], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Stun'] # list[str](optional)
    )
    
    return this_item