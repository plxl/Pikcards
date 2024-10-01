from ..bases.item import *

class DecorGiftBox(Item):
    pass


def load_me():
    this_item = DecorGiftBox(
        set = "C", # str
        number = 4, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Decor Gift Box", # str
        image = "04_Decor_Gift_Box.png", # str
        cardclass = 5, # int
        base_energy = 1, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Random Gift', 'Decor Pikmin'] # list[str](optional)
    )
    
    return this_item