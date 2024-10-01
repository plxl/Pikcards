from ..bases.item import *

class UltraBitterSpray(Item):
    pass


def load_me():
    this_item = UltraBitterSpray(
        set = "2", # str
        number = 96, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Ultra-Bitter Spray", # str
        image = "096_Ultra-Bitter_Spray.png", # str
        cardclass = 3, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Weightless', 'Rockify'] # list[str](optional)
    )
    
    return this_item