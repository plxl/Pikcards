from ..bases.item import *

class StellarOrb(Item):
    pass


def load_me():
    this_item = StellarOrb(
        set = "2", # str
        number = 84, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Stellar Orb", # str
        image = "084_Stellar_Orb.png", # str
        cardclass = 2, # int
        base_energy = 1, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Illuminate', 'Blinding Flash'] # list[str](optional)
    )
    
    return this_item