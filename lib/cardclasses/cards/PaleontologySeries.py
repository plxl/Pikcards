from ..bases.item import *

class PaleontologySeries(Item):
    pass


def load_me():
    this_item = PaleontologySeries(
        set = "2", # str
        number = 60, # int
        fifth = True, # bool
        rarity = 0, # int
        name = "Paleontology Series", # str
        image = "060_Paleontology_Series.png", # str
        cardclass = 5, # int
        base_energy = 1, # int
        base_time = 2, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Digging', 'Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Dig up'] # list[str](optional)
    )
    
    return this_item