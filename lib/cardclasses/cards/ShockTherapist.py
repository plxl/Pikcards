from ..bases.item import *

class ShockTherapist(Item):
    pass


def load_me():
    this_item = ShockTherapist(
        set = "2", # str
        number = 91, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Shock Therapist", # str
        image = "091_Shock_Therapist.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = ['"Electricity"'], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Stun'] # list[str](optional)
    )
    
    return this_item