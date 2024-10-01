from ..bases.item import *

class AncientAdSeries(Item):
    pass


def load_me():
    this_item = AncientAdSeries(
        set = "2", # str
        number = 76, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Ancient Ad Series", # str
        image = "076_Ancient_Ad_Series.png", # str
        cardclass = 5, # int
        base_energy = 4, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_item