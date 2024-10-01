from ..bases.item import *

class SucculentSeries(Item):
    pass


def load_me():
    this_item = SucculentSeries(
        set = "2", # str
        number = 55, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Succulent Series", # str
        image = "055_Succulent_Series.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Heal'] # list[str](optional)
    )
    
    return this_item