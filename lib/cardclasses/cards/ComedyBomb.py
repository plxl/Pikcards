from ..bases.item import *

class ComedyBomb(Item):
    pass


def load_me():
    this_item = ComedyBomb(
        set = "2", # str
        number = 93, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "Comedy Bomb", # str
        image = "093_Comedy_Bomb.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = ['Poison'], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Petrify'] # list[str](optional)
    )
    
    return this_item