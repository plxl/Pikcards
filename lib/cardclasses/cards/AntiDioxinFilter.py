from ..bases.item import *

class AntiDioxinFilter(Item):
    pass


def load_me():
    this_item = AntiDioxinFilter(
        set = "1", # str
        number = 50, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Anti-Dioxin Filter", # str
        image = "50_Anti-Dioxin_Filter.png", # str
        cardclass = 3, # int
        base_energy = 2, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = ['Fire', 'Water', 'Electricity', 'Poison'], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = [] # list[str](optional)
    )
    
    return this_item