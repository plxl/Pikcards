from ..bases.item import *

class SphericalAtlas(Item):
    pass


def load_me():
    this_item = SphericalAtlas(
        set = "2", # str
        number = 78, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Spherical Atlas", # str
        image = "078_Spherical_Atlas.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_item