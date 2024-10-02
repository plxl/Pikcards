from ..bases.item import *

class ModernAmenitiesSeries(Item):
    pass


def load_me():
    this_item = ModernAmenitiesSeries(
        set = "2", # str
        number = 64, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Modern Amenities Series", # str
        image = "064_Modern_Amenities_Series.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Return Boost'] # list[str](optional)
    )
    
    return this_item