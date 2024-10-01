from ..bases.item import *

class testitem1(Item):
    pass


def load_me():
    this_item = testitem1(
        set = "C", # str
        number = 27, # int
        fifth = True, # bool
        rarity = 2, # int
        name = "test_item_1", # str
        image = "27_test_item_1.png", # str
        cardclass = 5, # int
        base_energy = 1, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_item