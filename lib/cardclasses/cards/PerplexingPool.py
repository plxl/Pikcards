from ..bases.area import *

class PerplexingPool(Area):
    pass


def load_me():
    this_area = PerplexingPool(
        set = "2", # str
        number = 105, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Perplexing Pool", # str
        image = "105_Perplexing_Pool.png", # str
        cardclass = 2, # int
        base_energy = 3, # int
        base_time = 9, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Perplexing Pool'] # list[str](optional)
    )
    
    return this_area