from ..bases.item import *

class FivemanNapsack(Item):
    pass


def load_me():
    this_item = FivemanNapsack(
        set = "2", # str
        number = 81, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Five-man Napsack", # str
        image = "081_Five-man_Napsack.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Heal'] # list[str](optional)
    )
    
    return this_item