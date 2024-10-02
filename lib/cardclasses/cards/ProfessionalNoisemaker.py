from ..bases.item import *

class ProfessionalNoisemaker(Item):
    pass


def load_me():
    this_item = ProfessionalNoisemaker(
        set = "2", # str
        number = 89, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Professional Noisemaker", # str
        image = "089_Professional_Noisemaker.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = ['Piercing'], # list[str]
        immunities = [], # list[str]
        traits = ['Indirect', 'Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Uproot'] # list[str](optional)
    )
    
    return this_item