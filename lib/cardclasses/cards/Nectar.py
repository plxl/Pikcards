from ..bases.item import *

class Nectar(Item):
    pass


def load_me():
    this_item = Nectar(
        set = "1", # str
        number = 70, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Nectar", # str
        image = "70_Nectar.png", # str
        cardclass = 3, # int
        base_energy = 1, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Weightless', 'Overheal', 'Owner-able'] # list[str](optional)
    )
    
    return this_item