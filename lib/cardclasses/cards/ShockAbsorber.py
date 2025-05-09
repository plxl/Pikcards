from ..bases.item import *

class ShockAbsorber(Item):
    pass


def load_me():
    this_item = ShockAbsorber(
        set = "1", # str
        number = 45, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Shock Absorber", # str
        image = "45_Shock_Absorber.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Substitute'] # list[str](optional)
    )
    
    return this_item