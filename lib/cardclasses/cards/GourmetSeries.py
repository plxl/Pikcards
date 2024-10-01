from ..bases.item import *

class GourmetSeries(Item):
    pass


def load_me():
    this_item = GourmetSeries(
        set = "2", # str
        number = 58, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Gourmet Series", # str
        image = "058_Gourmet_Series.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Gourmand'] # list[str](optional)
    )
    
    return this_item