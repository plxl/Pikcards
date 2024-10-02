from ..bases.item import *

class _2IoniumJet(Item):
    pass


def load_me():
    this_item = _2IoniumJet(
        set = "1", # str
        number = 54, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "#2 Ionium Jet", # str
        image = "54_#2_Ionium_Jet.png", # str
        cardclass = 4, # int
        base_energy = 1, # int
        base_time = 1, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Multi-Attack', 'Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Synergy'] # list[str](optional)
    )
    
    return this_item