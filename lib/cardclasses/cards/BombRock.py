from ..bases.item import *

class BombRock(Item):
    pass


def load_me():
    this_item = BombRock(
        set = "1", # str
        number = 71, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Bomb Rock", # str
        image = "71_Bomb_Rock.png", # str
        cardclass = 4, # int
        base_energy = 2, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Explosive', 'Indirect'], # list[str]
        weakness_descriptions = ['Water'], # list[str](optional)
        ability_descriptions = ['One-Time Use'] # list[str](optional)
    )
    
    return this_item