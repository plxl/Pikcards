from ..bases.item import *

class NovaBlaster(Item):
    pass


def load_me():
    this_item = NovaBlaster(
        set = "1", # str
        number = 44, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Nova Blaster", # str
        image = "44_Nova_Blaster.png", # str
        cardclass = 1, # int
        base_energy = 4, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike', 'Indirect', 'Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item