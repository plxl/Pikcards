from ..bases.item import *

class SurvivalSeries(Item):
    pass


def load_me():
    this_item = SurvivalSeries(
        set = "2", # str
        number = 75, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Survival Series", # str
        image = "075_Survival_Series.png", # str
        cardclass = 1, # int
        base_energy = 3, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['"Debt Treasure"'], # list[str]
        weakness_descriptions = ['Poison', 'Mushroom'], # list[str](optional)
        ability_descriptions = ['Overheal'] # list[str](optional)
    )
    
    return this_item