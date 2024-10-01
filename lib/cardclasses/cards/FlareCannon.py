from ..bases.item import *

class FlareCannon(Item):
    pass


def load_me():
    this_item = FlareCannon(
        set = "2", # str
        number = 92, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Flare Cannon", # str
        image = "092_Flare_Cannon.png", # str
        cardclass = 2, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = ['"Fire"'], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Panic'] # list[str](optional)
    )
    
    return this_item