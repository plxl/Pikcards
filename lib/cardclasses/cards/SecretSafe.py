from ..bases.item import *

class SecretSafe(Item):
    pass


def load_me():
    this_item = SecretSafe(
        set = "1", # str
        number = 69, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Secret Safe", # str
        image = "69_Secret_Safe.png", # str
        cardclass = 4, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Dolphin Part"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Card Pull'] # list[str](optional)
    )
    
    return this_item