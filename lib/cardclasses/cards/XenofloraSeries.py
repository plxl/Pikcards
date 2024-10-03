from ..bases.item import *

class XenofloraSeries(Item):
    pass


def load_me():
    this_item = XenofloraSeries(
        set = "2", # str
        number = 57, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Xenoflora Series", # str
        image = "057_Xenoflora_Series.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Passive', 'Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Health Boost'] # list[str](optional)
    )
    
    return this_item