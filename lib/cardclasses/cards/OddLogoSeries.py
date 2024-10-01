from ..bases.item import *

class OddLogoSeries(Item):
    pass


def load_me():
    this_item = OddLogoSeries(
        set = "2", # str
        number = 77, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Odd Logo Series", # str
        image = "077_Odd_Logo_Series.png", # str
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