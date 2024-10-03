from ..bases.item import *

class MainEngine(Item):
    pass


def load_me():
    this_item = MainEngine(
        set = "1", # str
        number = 40, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Main Engine", # str
        image = "40_Main_Engine.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Energy Boost', 'Dolphin Synergy'] # list[str](optional)
    )
    
    return this_item