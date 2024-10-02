from ..bases.item import *

class NaturesCandySeries(Item):
    pass


def load_me():
    this_item = NaturesCandySeries(
        set = "2", # str
        number = 56, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Nature's Candy Series", # str
        image = "056_Nature's_Candy_Series.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive', 'Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Power Boost'] # list[str](optional)
    )
    
    return this_item