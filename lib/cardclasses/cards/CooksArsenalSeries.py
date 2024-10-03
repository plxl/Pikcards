from ..bases.item import *

class CooksArsenalSeries(Item):
    pass


def load_me():
    this_item = CooksArsenalSeries(
        set = "2", # str
        number = 62, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Cook's Arsenal Series", # str
        image = "062_Cook's_Arsenal_Series.png", # str
        cardclass = 1, # int
        base_energy = 5, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Boost'] # list[str](optional)
    )
    
    return this_item