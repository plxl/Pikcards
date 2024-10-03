from ..bases.item import *

class RadiationCanopy(Item):
    pass


def load_me():
    this_item = RadiationCanopy(
        set = "1", # str
        number = 63, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Radiation Canopy", # str
        image = "63_Radiation_Canopy.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = ['Explosive', 'Gloom'], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item