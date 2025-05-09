from ..bases.item import *

class MassageMachine(Item):
    pass


def load_me():
    this_item = MassageMachine(
        set = "1", # str
        number = 60, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "Massage Machine", # str
        image = "60_Massage_Machine.png", # str
        cardclass = 4, # int
        base_energy = 4, # int
        base_time = 3, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Dolphin Part'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Heal over time'] # list[str](optional)
    )
    
    return this_item