from ..bases.item import *

class _1IoniumJet(Item):
    pass


def load_me():
    this_item = _1IoniumJet(
        set = "1", # str
        number = 53, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "#1 Ionium Jet", # str
        image = "53_#1_Ionium_Jet.png", # str
        cardclass = 4, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['First Strike', 'Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Synergy'] # list[str](optional)
    )
    
    return this_item