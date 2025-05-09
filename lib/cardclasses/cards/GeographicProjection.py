from ..bases.item import *

class GeographicProjection(Item):
    pass


def load_me():
    this_item = GeographicProjection(
        set = "2", # str
        number = 79, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Geographic Projection", # str
        image = "079_Geographic_Projection.png", # str
        cardclass = 5, # int
        base_energy = 3, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Debt Treasure'], # list[str]
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Conjure'] # list[str](optional)
    )
    
    return this_item