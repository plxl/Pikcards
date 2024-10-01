from ..bases.area import *

class AwakeningWood(Area):
    pass


def load_me():
    this_area = AwakeningWood(
        set = "2", # str
        number = 104, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Awakening Wood", # str
        image = "104_Awakening_Wood.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Awakening Wood'] # list[str](optional)
    )
    
    return this_area