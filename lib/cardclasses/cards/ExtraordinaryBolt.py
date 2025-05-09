from ..bases.item import *

class ExtraordinaryBolt(Item):
    pass


def load_me():
    this_item = ExtraordinaryBolt(
        set = "1", # str
        number = 43, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Extraordinary Bolt", # str
        image = "43_Extraordinary_Bolt.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item