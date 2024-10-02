from ..bases.item import *

class JusticeAlloy(Item):
    pass


def load_me():
    this_item = JusticeAlloy(
        set = "2", # str
        number = 87, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Justice Alloy", # str
        image = "087_Justice_Alloy.png", # str
        cardclass = 3, # int
        base_energy = 4, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Metal Suit Z'] # list[str](optional)
    )
    
    return this_item