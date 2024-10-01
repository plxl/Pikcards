from ..bases.item import *

class TreasureinaBottle(Item):
    pass


def load_me():
    this_item = TreasureinaBottle(
        set = "C", # str
        number = 18, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Treasure in a Bottle", # str
        image = "18_Treasure_in_a_Bottle.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = ['"Explosive"', '"Gloom"'], # list[str]
        traits = [], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_item