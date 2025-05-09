from ..bases.area import *

class TheForestofHope(Area):
    pass


def load_me():
    this_area = TheForestofHope(
        set = "1", # str
        number = 77, # int
        fifth = True, # bool
        rarity = 1, # int
        name = "The Forest of Hope", # str
        image = "77_The_Forest_of_Hope.png", # str
        cardclass = 1, # int
        base_energy = 2, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = [], # list[str]
        description = "Description", # str
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Forest of Hope'] # list[str](optional)
    )
    
    return this_area