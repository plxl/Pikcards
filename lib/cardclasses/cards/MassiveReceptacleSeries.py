from ..bases.item import *

class MassiveReceptacleSeries(Item):
    pass


def load_me():
    this_item = MassiveReceptacleSeries(
        set = "2", # str
        number = 74, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Massive Receptacle Series", # str
        image = "074_Massive_Receptacle_Series.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Defense"', '"Debt Treasure"'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Weightless', 'Return'] # list[str](optional)
    )
    
    return this_item