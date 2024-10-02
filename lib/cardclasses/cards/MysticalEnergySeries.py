from ..bases.item import *

class MysticalEnergySeries(Item):
    pass


def load_me():
    this_item = MysticalEnergySeries(
        set = "2", # str
        number = 73, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Mystical Energy Series", # str
        image = "073_Mystical_Energy_Series.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 6, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Energy Boost'] # list[str](optional)
    )
    
    return this_item