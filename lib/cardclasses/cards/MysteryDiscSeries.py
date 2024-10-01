from ..bases.item import *

class MysteryDiscSeries(Item):
    pass


def load_me():
    this_item = MysteryDiscSeries(
        set = "C", # str
        number = 28, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Mystery Disc Series", # str
        image = "28_Mystery_Disc_Series.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Cover'] # list[str](optional)
    )
    
    return this_item