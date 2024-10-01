from ..bases.area import *

class play4(Area):
    pass


def load_me():
    this_area = play4(
        set = "C", # str
        number = 31, # int
        fifth = False, # bool
        rarity = 0, # int
        name = "play_4", # str
        image = "31_play_4.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 4, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['play_4'] # list[str](optional)
    )
    
    return this_area