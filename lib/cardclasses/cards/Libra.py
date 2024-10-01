from ..bases.item import *

class Libra(Item):
    pass


def load_me():
    this_item = Libra(
        set = "1", # str
        number = 47, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Libra", # str
        image = "47_Libra.png", # str
        cardclass = 4, # int
        base_energy = 1, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Dolphin Part"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Distribute Power'] # list[str](optional)
    )
    
    return this_item