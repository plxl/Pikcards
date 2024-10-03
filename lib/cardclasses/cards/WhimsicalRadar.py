from ..bases.item import *

class WhimsicalRadar(Item):
    pass


def load_me():
    this_item = WhimsicalRadar(
        set = "1", # str
        number = 42, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Whimsical Radar", # str
        image = "42_Whimsical_Radar.png", # str
        cardclass = 2, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Search Area'] # list[str](optional)
    )
    
    return this_item