from ..bases.minion import *

class SegmentedCrawbster(Minion):
    pass


def load_me():
    this_minion = SegmentedCrawbster(
        set = "2", # str
        number = 51, # int
        fifth = False, # bool
        rarity = 1, # int
        name = "Segmented Crawbster", # str
        image = "051_Segmented_Crawbster.png", # str
        cardclass = 1, # int
        base_energy = 7, # int
        base_time = 5, # int
        elements = [], # list[str]
        immunities = [], # list[str]
        traits = ['Defense'], # list[str]
        base_attack = 7, # int
        base_health = 4, # int
        defense = 1, # int
        maxcarry = 1, # int
        weakness_descriptions = [], # list[str](optional)
        ability_descriptions = ['Rockfall', 'Reckless Roll'] # list[str](optional)
    )
    
    return this_minion