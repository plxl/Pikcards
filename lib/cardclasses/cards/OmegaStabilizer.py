from ..bases.item import *

class OmegaStabilizer(Item):
    pass


def load_me():
    this_item = OmegaStabilizer(
        set = "1", # str
        number = 65, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Omega Stabilizer", # str
        image = "65_Omega_Stabilizer.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Move'] # list[str](optional)
    )
    
    return this_item